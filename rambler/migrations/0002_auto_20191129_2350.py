# Generated by Django 2.2.5 on 2019-11-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rambler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='target',
            name='ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
