# Generated by Django 2.2.5 on 2019-12-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
