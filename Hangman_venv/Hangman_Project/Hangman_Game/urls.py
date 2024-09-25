from django.urls import path
from . import views


urlpatterns = [
    path('',views.HangmanHome,name='HangmanHome'),
    path('Hangman',views.Hangman,name='Hangman')
]