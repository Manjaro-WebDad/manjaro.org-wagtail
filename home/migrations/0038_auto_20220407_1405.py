# Generated by Django 3.2.12 on 2022-04-07 14:05

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0037_sponsors_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('partners', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Vendor', required=True)), ('description', wagtail.core.blocks.TextBlock(help_text='Short Vendor Description', required=True)), ('details', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True)),
                ('intro', models.TextField(blank=True, default='', max_length=150)),
                ('keywords', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='Sponsors',
        ),
    ]
