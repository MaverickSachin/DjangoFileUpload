# Generated by Django 3.0.7 on 2020-06-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
