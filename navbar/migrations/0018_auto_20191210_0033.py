# Generated by Django 2.2.5 on 2019-12-09 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0017_auto_20191106_1435'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ad',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='open_hours',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='carrepair',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='e_store',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='navigation',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='open_hours',
        ),
        migrations.RemoveField(
            model_name='navbar_lang',
            name='repair',
        ),
    ]
