from rest_framework import serializers
from NoteService.models import Note, Tag
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin


class NoteDetailSerializer(serializers.ModelSerializer):
    note_author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    note_editTime = serializers.HiddenField(default=timezone.now)

    class Meta:
        model = Note
        fields = ('note_name', 'note_text', 'note_author', 'note_editTime')


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'note_name', 'note_author', 'note_text', 'note_editTime', 'tags')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
