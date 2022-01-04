# Generated by Django 3.2.9 on 2021-11-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50)),
                ('comment_content', models.CharField(max_length=500)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
    ]
