# Generated by Django 5.1.7 on 2025-04-03 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_socialmedia_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinformation',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='myinformation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='myinformation',
            name='map_embed_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myinformation',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_medias', to='about.myinformation'),
        ),
    ]
