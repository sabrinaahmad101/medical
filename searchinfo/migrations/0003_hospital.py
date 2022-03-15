# Generated by Django 3.1 on 2020-09-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchinfo', '0002_booking1'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitsl_name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('Bkash_no', models.CharField(max_length=10)),
                ('contact_no', models.IntegerField()),
            ],
        ),
    ]
