# Generated by Django 4.1.4 on 2022-12-25 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_client_mobile_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
