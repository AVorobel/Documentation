# Generated by Django 2.2.7 on 2019-11-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteService', '0002_auto_20191114_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
