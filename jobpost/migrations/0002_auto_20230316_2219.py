# Generated by Django 3.2.16 on 2023-03-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=150)),
                ('job_id', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('skill', models.CharField(max_length=150)),
                ('experience', models.CharField(max_length=150)),
                ('jsondata', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='hod',
        ),
    ]