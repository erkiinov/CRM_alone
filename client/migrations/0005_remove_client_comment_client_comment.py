# Generated by Django 4.0 on 2022-05-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Comment',
        ),
        migrations.AddField(
            model_name='client',
            name='comment',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
    ]
