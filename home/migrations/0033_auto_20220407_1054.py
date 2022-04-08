# Generated by Django 3.2.12 on 2022-04-07 10:54

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0032_sponsors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='content',
            field=wagtail.core.fields.StreamField([('sponsor', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Vendor', required=True)), ('description', wagtail.core.blocks.TextBlock(help_text='Short Vendor Description', required=True)), ('details', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True),
        ),
    ]