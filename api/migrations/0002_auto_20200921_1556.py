# Generated by Django 3.1.1 on 2020-09-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestImage',
        ),
        migrations.RemoveField(
            model_name='activitypicture',
            name='path',
        ),
        migrations.AddField(
            model_name='activitypicture',
            name='activity_picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]