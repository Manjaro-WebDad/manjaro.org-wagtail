# Generated by Django 3.2.10 on 2022-01-26 19:43

import customblocks.blocks
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220126_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', customblocks.blocks.RichtextBlock())], blank=True, null=True),
        ),
    ]
