# Generated by Django 3.0 on 2020-04-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0002_auto_20200429_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='status_reason',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
