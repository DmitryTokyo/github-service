import json
import requests
from django.conf import settings
from django.core.cache import cache


def get_pull_requests(username) -> json:
    url: str = 'https://api.github.com/search/issues'

    headers = {
        'Accept': 'application/vnd.github.preview',
        'Authorization': f'token {settings.GITHUB_TOKEN}'
    }

    payload = {
        'q': f'is:pr author:{username}',
        'per_page': 100,
    }

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    pull_requests = response.json()['items']

    user_pull_requests = {}
    for pull_request in pull_requests:
        repository_url = pull_request['repository_url']

        if not repository_url in user_pull_requests:
            user_pull_requests[repository_url] = []

        pull_merge = check_merge(pull_request['pull_request']['url'])
        user_pull_requests[repository_url].append({
            'pull_title': pull_request['title'],
            'pull_html_url': pull_request['pull_request']['html_url'],
            'merge': pull_merge,
            'comments_count': pull_request['comments']
        })
    
    return user_pull_requests


def check_merge(url) -> bool:
    headers = {
        'Accept': 'application/vnd.github.preview',
        'Authorization': f'token {settings.GITHUB_TOKEN}'
    }
    response = requests.get(f'{url}/merge', headers=headers)
    if response.status_code == 204:
        return True
    return False


def get_repositories_and_pulls(username) -> json:
    headers = {
        'Accept': 'application/vnd.github.preview',
        'Authorization': f'token {settings.GITHUB_TOKEN}'
    }
    pull_requests = get_pull_requests(username)
    
    repositories_and_pulls = {}
    for repository_url, pulls_info in pull_requests.items():
        response = requests.get(repository_url, headers=headers)
        response.raise_for_status()

        repository = response.json()
        repository_name = repository['name']
        repositories_and_pulls[repository_name] = {
                'repository_stars': repository['stargazers_count'],
                'repository_html_url': repository['html_url'],
                'pull_requests_info': pulls_info
            }
    return repositories_and_pulls


def get_user_repositories_and_names(username) -> tuple[json, str]:
    if not cache.get(username):
        user_repositories = get_repositories_and_pulls(username)
        cache.set(username, user_repositories)
    else:
        user_repositories = cache.get(username)

    repositories_names = [user_repository for user_repository in user_repositories]
    return user_repositories, repositories_names