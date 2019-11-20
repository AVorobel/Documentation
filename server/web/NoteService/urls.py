from django.contrib import admin
from django.urls import path, include
from NoteService.views import *

app_name = 'NoteService'
urlpatterns = [
    path('note/create/', NoteCreateView.as_view()),
    path('note/all/', NoteListView.as_view()),
    path('note/edit/<int:pk>/', NoteEditView.as_view()),
    path('user/create/', UserCreateView.as_view()),
]
