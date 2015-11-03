# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logID', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('site', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20)),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.IntegerField()),
                ('nickname', models.CharField(default=b'', max_length=16, null=True)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('qq', models.CharField(max_length=20)),
                ('home', models.CharField(max_length=50)),
                ('goal', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('number', models.IntegerField()),
                ('busy', models.IntegerField()),
                ('tip', models.CharField(default=b'', max_length=128, null=True)),
                ('question', models.CharField(default=b'', max_length=128, null=True)),
                ('answer', models.CharField(default=b'', max_length=128, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
