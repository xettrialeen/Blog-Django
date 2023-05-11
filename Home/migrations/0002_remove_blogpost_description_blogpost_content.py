# Generated by Django 4.2.1 on 2023-05-10 14:42

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='description',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=django_quill.fields.QuillField(null=True),
        ),
    ]
