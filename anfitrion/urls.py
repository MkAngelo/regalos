"""ANFITRION URL's"""
from django.urls import path
from anfitrion import views

urlpatterns = [
    path(
        route='home/',
        view=views.HomeView.as_view(),
        name='home'
    )
]
