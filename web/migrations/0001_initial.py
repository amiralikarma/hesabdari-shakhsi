# Generated by Django 3.2.13 on 2022-07-11 21:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('amount', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
