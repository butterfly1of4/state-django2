# Generated by Django 3.1.4 on 2020-12-04 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usacapitals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitals',
            old_name='captial',
            new_name='capital',
        ),
    ]
