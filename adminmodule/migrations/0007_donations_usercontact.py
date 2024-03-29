# Generated by Django 5.0.2 on 2024-03-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0006_remove_donar_donarid_alter_donar_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=100)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('raxorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'donardonations',
            },
        ),
        migrations.CreateModel(
            name='usercontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('comment', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
