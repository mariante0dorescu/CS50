from django.urls import path, include
from django.views.generic import RedirectView


from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", RedirectView.as_view(pattern_name='encyclopedia:title')),
    path("create/", views.create, name="create"),
    path("random/", views.random, name="random"),
    path("wiki/<str:title>", views.title, name='title'),
    path("wiki/<str:title>/edit", views.edit_title, name='edit_title')
]
