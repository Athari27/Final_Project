# Generated by Django 4.1.3 on 2022-11-15 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.BooleanField()),
                ('university_name', models.CharField(max_length=2048)),
                ('department', models.CharField(max_length=2048)),
                ('level', models.CharField(choices=[('6', '6'), ('7', '7'), ('8', '8')], max_length=64)),
            ],
        ),
    ]
