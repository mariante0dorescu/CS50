from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("categories/", lambda request: redirect('categories_all'), name="categories"),
    path("categories/all/", views.categories_all, name="categories_all"),
    path("categories/<str>", views.category, name="category"),
    path("watching/", views.watching_list, name="watching"),
    path("listing/<int:pk>", views.listing, name='listing'),
    path("listing/<int:pk>/watch", views.watch, name='watch'),
    path("listing/<int:pk>/unwatch", views.unwatch, name='unwatch'),
]
