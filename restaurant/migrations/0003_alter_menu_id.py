# Generated by Django 5.0.6 on 2024-08-31 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
