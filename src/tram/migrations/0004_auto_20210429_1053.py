# Generated by Django 3.1.7 on 2021-04-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0003_documentprocessingjob_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tram.document'),
        ),
    ]
