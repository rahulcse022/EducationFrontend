# Generated by Django 3.0.5 on 2021-08-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningApp', '0002_auto_20210729_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('courseids', models.CharField(max_length=1000)),
            ],
        ),
    ]