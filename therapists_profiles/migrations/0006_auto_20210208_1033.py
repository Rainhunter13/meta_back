# Generated by Django 3.1.6 on 2021-02-08 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapists_profiles', '0005_auto_20210208_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='therapist',
            old_name='therapist',
            new_name='sync_record',
        ),
    ]
