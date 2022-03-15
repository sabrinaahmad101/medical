# Generated by Django 3.1 on 2020-09-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchinfo', '0007_doctor1'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_news', models.BooleanField(default=False)),
                ('img_link', models.TextField()),
                ('news_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]