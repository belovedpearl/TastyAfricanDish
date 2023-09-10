# Generated by Django 3.2.20 on 2023-09-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0002_remove_recipe_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('country_approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]