from django.urls import path
from pulls.views import IndexView, RepositoriesView, PullsView, RegistrationView, LoginView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:username>/repositories', RepositoriesView.as_view(), name='repositories'),
    path('<str:username>/<str:repository_name>/pulls', PullsView.as_view(), name='pulls'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login')
]
