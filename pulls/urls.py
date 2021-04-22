from django.urls import path

from .views import IndexView, RepositoriesView, PullsView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:username>/repositories', views.RepositoriesView.as_view(), name='repositories'),
    path('<str:username>/<str:repository_name>/pulls', views.PullsView.as_view(), name='pulls'),
]
