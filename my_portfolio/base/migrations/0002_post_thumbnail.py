# Generated by Django 4.0.3 on 2022-11-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='project-mockup-example.jpeg', null=True, upload_to='images'),
        ),
    ]
