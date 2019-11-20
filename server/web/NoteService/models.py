from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Tag (models.Model):
    class Meta:
        db_table = "db_Tags"
    tag_name = models.CharField(max_length=30, blank=False, null=False,default="#")
    tag_note = models.ForeignKey('Note', related_name='tags', on_delete=models.CASCADE, null=True)


class Note (models.Model):
    class Meta:
        db_table = "db_Notes"
    note_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    note_text = models.CharField(max_length=404, blank=False, null=False)
    note_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    note_editTime = models.DateTimeField()
