# Generated by Django 4.2.14 on 2024-10-30 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0008_vulnerability_cve_alter_note_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('url', models.URLField(null=True)),
                ('description', models.CharField(max_length=600, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.date(2024, 10, 30)),
        ),
    ]
