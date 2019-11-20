# Generated by Django 2.2.7 on 2019-11-14 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='#', max_length=30)),
            ],
            options={
                'db_table': 'db_Tags',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_name', models.CharField(max_length=30)),
                ('note_text', models.CharField(max_length=404)),
                ('note_editTime', models.DateTimeField()),
                ('note_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('note_tag', models.ForeignKey(default='#note', on_delete=django.db.models.deletion.CASCADE, to='NoteService.Tag')),
            ],
            options={
                'db_table': 'db_Notes',
            },
        ),
    ]