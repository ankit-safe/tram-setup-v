# Generated by Django 3.1.7 on 2021-04-29 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0004_auto_20210429_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tram.document'),
        ),
    ]
