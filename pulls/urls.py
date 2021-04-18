from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/repositories', views.get_projects, name='repositories'),
    path('<str:username>/<str:repository_name>/pulls', views.get_project_pulls, name='pulls'),
]
