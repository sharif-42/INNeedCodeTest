# Generated by Django 3.0.2 on 2020-01-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_detector', '0005_auto_20200129_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.ImageField(upload_to='images'),
        ),
    ]