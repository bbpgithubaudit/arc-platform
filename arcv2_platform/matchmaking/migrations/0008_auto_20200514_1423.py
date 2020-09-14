# Generated by Django 3.0 on 2020-05-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0007_auto_20200511_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status_reason',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='status_reason_sensitive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('open', 'Open'), ('closed', 'Closed'), ('archived', 'Archived'), ('rejected', 'Rejected')], default='submitted', max_length=10),
        ),
    ]
