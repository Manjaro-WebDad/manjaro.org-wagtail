# Generated by Django 3.2.12 on 2022-03-23 10:48

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_auto_20220322_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title'),
        ),
    ]