# Generated by Django 4.1 on 2022-08-15 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_Ьirth',
            new_name='date_of_birth',
        ),
    ]
