# Generated by Django 4.1 on 2022-08-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_date_of_ьirth_author_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author1',
        ),
    ]
