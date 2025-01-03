# Generated by Django 4.2.14 on 2024-11-09 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0010_alter_note_content_alter_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='status',
            field=models.CharField(choices=[('Intact', 'Intact'), ('Foothold', 'Foothold'), ('Rooted', 'Rooted')], default='Intact', max_length=8),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.date(2024, 11, 9)),
        ),
    ]
