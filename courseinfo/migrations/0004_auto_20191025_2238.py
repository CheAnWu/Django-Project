# Generated by Django 2.2.5 on 2019-10-25 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_auto_20190921_2241'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('semester', 'course', 'section_name')},
        ),
    ]
