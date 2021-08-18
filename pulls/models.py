from django.db import models
from django.contrib.auth.models import User


class GithubUser(models.Model):
    user = models.OneToOneField(User, related_name='requests', on_delete=models.CASCADE)
    github_username = models.CharField('Github username', max_length=50)
    requested_at = models.DateTimeField('Request time', auto_now_add=True)


class SearchResult(models.Model):
    result = models.JSONField('Result of search')
    request = models.OneToOneField(GithubUser, on_delete=models.CASCADE, related_name='request')
