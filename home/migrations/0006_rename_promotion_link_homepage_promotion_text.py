# Generated by Django 3.2.13 on 2022-04-18 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220418_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='promotion_link',
            new_name='promotion_text',
        ),
    ]