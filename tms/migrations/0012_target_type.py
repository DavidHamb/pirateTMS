# Generated by Django 4.2.14 on 2024-11-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0011_target_status_alter_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='type',
            field=models.CharField(choices=[('Capture the Flag', 'Ctf'), ('In the Wild', 'Wild'), ('Bug Bounty', 'Bug Bounty')], default='In the wild', max_length=16),
        ),
    ]
