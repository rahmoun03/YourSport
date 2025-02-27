# Generated by Django 5.1.6 on 2025-02-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auth_db',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=10000)),
                ('activation', models.BooleanField(default=False)),
            ],
        ),
    ]
