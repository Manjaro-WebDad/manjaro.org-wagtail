# Generated by Django 3.2.12 on 2022-03-23 11:12

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0013_auto_20220323_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]