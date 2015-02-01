# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('birthday', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=13)),
                ('sex', models.CharField(max_length=10)),
                ('birthday', models.DateTimeField(null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='base.City', null=True)),
                ('district', models.ForeignKey(blank=True, to='base.District', null=True)),
                ('province', models.ForeignKey(blank=True, to='base.Province', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diary_frequency', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='parents',
            name='settings',
            field=models.OneToOneField(to='baby.Settings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parents',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baby',
            name='parents',
            field=models.ForeignKey(to='baby.Parents'),
            preserve_default=True,
        ),
    ]
