# Generated by Django 2.1 on 2020-07-22 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPicture',
            fields=[
                ('activity_picture_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateField()),
                ('place', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('limit', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='StudyMember',
            fields=[
                ('study_member_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('study_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.Study')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('cellphone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('user_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.Category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='studymember',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.User'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='study_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.Study'),
        ),
        migrations.AddField(
            model_name='activitypicture',
            name='study_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisestudy_app.Study'),
        ),
    ]
