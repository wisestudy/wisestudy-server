# Generated by Django 2.2.13 on 2020-09-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_schedule_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]