# Generated by Django 2.2.9 on 2020-01-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200114_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='vision_and_mission',
            field=models.TextField(blank=True, default='UMA Vision and Mission', null=True),
        ),
    ]
