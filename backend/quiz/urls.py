from django.urls import include, path
from .views import GenerateQuizView
urlpatterns = [
    path("generate/", view=GenerateQuizView.as_view())
]
