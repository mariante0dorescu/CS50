from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
  #path("", views.index, name="index"),
  path("", views.IndexView.as_view(), name="index"),
  path("<int:pk>/", views.DetailView.as_view(), name="detail"),
  path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
  path("<int:question_id>/vote/", views.vote, name="vote"),
]

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)