# Generated by Django 3.0 on 2020-08-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_requester'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notification_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
