# Generated by Django 3.2.20 on 2023-09-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='status',
        ),
    ]
