# Generated by Django 2.2.5 on 2019-09-21 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20190921_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='instructor_id',
            new_name='instructor',
        ),
    ]
