# Generated by Django 3.2.15 on 2024-05-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuwallsproducts', '0009_confirmbooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmbooking',
            name='status',
            field=models.CharField(choices=[('BOOKING', 'Booking created but didnt recieve by the user'), ('BORROWED', 'Borrowed'), ('RETURNED', 'Returned')], default='BOOKING', max_length=10),
        ),
    ]
