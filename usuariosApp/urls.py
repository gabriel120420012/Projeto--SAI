from django.urls import path
from  django.contrib.auth import views as auth_views
from .views import criar_usuario

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='cpasis/home.html'
    ), name='logout'),

    path('criar_usuario/', criar_usuario,name='criar_usuario'),
]