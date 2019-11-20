from django.shortcuts import render
from rest_framework import generics, viewsets
from NoteService.serializers import *
from NoteService.models import Note
from NoteService.permissions import *
from rest_framework.permissions import IsAuthenticated
from djoser.serializers import UserCreateSerializer


class NoteCreateView(generics.CreateAPIView):
    serializer_class = NoteDetailSerializer


class NoteListView(generics.ListAPIView):
    serializer_class = NoteListSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated, )


class SetPermissioView(generics.CreateAPIView):
    ...


class NoteEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
    permission_classes = (HasPermissionOrReadOnly, )


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


