# Generated by Django 3.0.5 on 2021-07-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='button',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='coursename',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='fulldesc',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='sortdesc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='trainer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='addcourse',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]