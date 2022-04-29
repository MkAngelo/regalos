"""ANFITRION URL's"""
from django.urls import path
from anfitrion import views

urlpatterns = [
    path(
        route='menu/',
        view=views.MenuView.as_view(),
        name='menu'
    ),
    path(
        route='signup/',
        view=views.SignUpView.as_view(),
        name='signup'
    ),
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='crear/',
        view=views.create_view,
        name='crear'
    ),
]
