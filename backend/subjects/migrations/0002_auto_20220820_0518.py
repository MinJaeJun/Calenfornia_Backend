# Generated by Django 3.2 on 2022-08-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='classnum',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='professor',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_title',
            field=models.TextField(),
        ),
    ]