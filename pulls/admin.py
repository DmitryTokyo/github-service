from django.contrib import admin

from pulls.models import GithubUser, SearchResult


@admin.register(GithubUser)
class GithubUserAdmin(admin.ModelAdmin):
    model = GithubUser


@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    model = SearchResult