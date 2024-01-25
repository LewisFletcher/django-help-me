# Generated by Django 5.0 on 2024-01-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_docs', '0002_alter_documentation_reference_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='keywords',
            field=models.TextField(blank=True, help_text='Comma separated list of keywords to help users find this documentation.'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentation',
            name='keywords',
            field=models.TextField(blank=True, help_text='Comma separated list of keywords to help users find this documentation.'),
        ),
    ]
