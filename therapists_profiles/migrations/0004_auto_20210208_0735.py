# Generated by Django 3.1.6 on 2021-02-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists_profiles', '0003_auto_20210207_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='therapist',
            field=models.ManyToManyField(related_name='methods', to='therapists_profiles.Therapist'),
        ),
    ]
