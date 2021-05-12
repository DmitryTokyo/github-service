from django.shortcuts import render, redirect
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import View, DetailView
import requests

import os
from pulls.github import get_user_repositories_and_names


class IndexView(View):
    def get(self, request):
        try:
            wrong_username = request.session['error']
            del request.session['error']
        except KeyError:
            wrong_username = None

        context = {
            'wrong_username': wrong_username
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        username = request.POST['username']
        try:
            request.session[username]
        except KeyError:
            cache.clear()

        request.session[username] = username
        return redirect('repositories', username=username)
    

class RepositoriesView(DetailView):
    def get(self, request, username):
        try:
            user_repositories, repositories_names = get_user_repositories_and_names(username)
        except requests.exceptions.HTTPError:
            request.session['error'] = username
            return redirect('/')

        cache.set(f'{username}_merge_status', True)
        page_paginator = Paginator(repositories_names, 10)
        page_number = request.GET.get('page', 1)

        try:
            repositories_names = page_paginator.page(page_number)
        except EmptyPage:
            repositories_names = page_paginator.page(1)

        context = { 
            'username': username,
            'repositories_names': repositories_names,
        }
        return render(request, 'repositories.html', context=context)


class PullsView(View):
    def get(self, request, username, repository_name):
        user_repositories, _ = get_user_repositories_and_names(username)
        repository = user_repositories[repository_name]

        is_merged = cache.get(f'{username}_merge_status')
        pulls = [pull for pull in repository['pull_requests_info'] if pull['merge'] == is_merged]
        
        page_paginator = Paginator(pulls, 10)
        page_number = request.GET.get('page', 1)
        try:
            pulls = page_paginator.page(page_number)
        except EmptyPage:
            pulls = page_paginator.page(1)

        context = {
            'username': username,
            'repository_name': repository_name,
            'repository': repository,
            'pulls': pulls,
            'is_merged': is_merged
        }
        return render(request, 'pull_requests.html', context=context)

    def post(self, request, username, repository_name):
        if request.POST['is_merged'] == 'unmerged pulls':
            is_merged = False
        if request.POST['is_merged'] == 'merged pulls':
            is_merged = True
        cache.set(f'{username}_merge_status', is_merged, 3600)
        return redirect('pulls', username=username, repository_name=repository_name)



