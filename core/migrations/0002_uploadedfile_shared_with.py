# Generated by Django 3.2.13 on 2023-12-09 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_files', to=settings.AUTH_USER_MODEL),
        ),
    ]
