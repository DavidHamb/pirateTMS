# Generated by Django 4.2.14 on 2024-10-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0006_alter_vulnerability_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='hostname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]