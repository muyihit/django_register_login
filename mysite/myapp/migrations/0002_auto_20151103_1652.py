# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('siteID', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strategyID', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='log',
            old_name='userID',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='logID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='site',
            field=models.OneToOneField(to='myapp.Site'),
        ),
    ]
