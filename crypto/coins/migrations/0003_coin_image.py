# Generated by Django 4.1.7 on 2023-02-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_remove_coin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
