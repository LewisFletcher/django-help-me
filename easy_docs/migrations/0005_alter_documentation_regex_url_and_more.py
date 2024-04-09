# Generated by Django 5.0 on 2024-04-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_docs', '0004_documentation_regex_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='regex_url',
            field=models.CharField(blank=True, help_text="Regular expression to match the URL of the page you are documenting, if any. Leave blank if this isn't needed.", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historicaldocumentation',
            name='regex_url',
            field=models.CharField(blank=True, help_text="Regular expression to match the URL of the page you are documenting, if any. Leave blank if this isn't needed.", max_length=200, null=True),
        ),
    ]
