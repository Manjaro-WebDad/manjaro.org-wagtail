# Generated by Django 3.2.12 on 2022-04-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_homepage_feature_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='feature_one',
        ),
        migrations.AddField(
            model_name='homepage',
            name='footer_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='manjaro_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='manjaro_title',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partners_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partners_title',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partners_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='shells_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='shells_title',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]