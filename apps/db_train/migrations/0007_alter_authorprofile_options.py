# Generated by Django 4.2.5 on 2024-03-28 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0006_remove_tag_tags_entry_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorprofile',
            options={'verbose_name': 'Профиль автора', 'verbose_name_plural': 'Профили авторов'},
        ),
    ]
