# Generated by Django 5.0.4 on 2024-05-23 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.tag'),
        ),
    ]
