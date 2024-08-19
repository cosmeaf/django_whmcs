# Generated by Django 5.1 on 2024-08-18 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=255, unique=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('gid', models.IntegerField(blank=True, null=True)),
                ('home_directory', models.CharField(max_length=255)),
                ('shell', models.CharField(default='/bin/sh', max_length=100)),
                ('group', models.CharField(default='www-data', max_length=150)),
                ('comment', models.CharField(default='User Web Data Manager', max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('account_expiry', models.DateTimeField(blank=True, null=True)),
                ('password_expiry', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_password_change', models.DateTimeField(blank=True, null=True)),
                ('inactive', models.BooleanField(default=False)),
                ('sudo_access', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdomain', models.CharField(max_length=255, unique=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.member')),
            ],
            options={
                'verbose_name': 'Subdominio',
                'verbose_name_plural': 'Subdominios',
                'ordering': ['subdomain'],
            },
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['username'], name='user_manage_usernam_2b395d_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['uid'], name='user_manage_uid_41c218_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['gid'], name='user_manage_gid_68eeb7_idx'),
        ),
        migrations.AddIndex(
            model_name='domain',
            index=models.Index(fields=['subdomain'], name='user_manage_subdoma_35ee76_idx'),
        ),
    ]
