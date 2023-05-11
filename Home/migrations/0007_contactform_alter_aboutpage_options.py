# Generated by Django 4.2.1 on 2023-05-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name_plural': 'About Page'},
        ),
    ]
