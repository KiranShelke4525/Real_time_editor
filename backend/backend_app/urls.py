from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/user/', UserView.as_view()),
    path('api/my-documents/', MyDocumentsView.as_view()),
    path("api/correct-text/", LanguageToolCorrectView.as_view()),
]
