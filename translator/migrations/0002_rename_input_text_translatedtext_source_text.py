# Generated by Django 4.2.4 on 2023-08-14 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translatedtext',
            old_name='input_text',
            new_name='source_text',
        ),
    ]
