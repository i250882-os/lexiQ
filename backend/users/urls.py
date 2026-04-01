from .views import LoginView, RefreshView
from django.urls import path

urlpatterns = [
    path('token/', LoginView.as_view()),
    path('token/refresh/', RefreshView.as_view()),  
]
