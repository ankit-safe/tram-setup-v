# Generated by Django 3.2.6 on 2021-12-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0009_auto_20211209_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackobject',
            name='attack_type',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attackobject',
            name='stix_type',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
