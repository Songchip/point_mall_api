# Generated by Django 2.2.3 on 2019-07-25 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to=settings.AUTH_USER_MODEL),
        ),
    ]
