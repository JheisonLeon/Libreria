# Generated by Django 3.0.6 on 2023-04-30 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Telematicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='description',
            new_name='descripcion',
        ),
    ]
