# Generated by Django 4.1.6 on 2023-02-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baham', '0003_vehicle_picture1_vehicle_picture2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='picture1',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='picture2',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
    ]
