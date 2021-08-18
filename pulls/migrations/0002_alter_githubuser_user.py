# Generated by Django 3.2 on 2021-05-13 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pulls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
