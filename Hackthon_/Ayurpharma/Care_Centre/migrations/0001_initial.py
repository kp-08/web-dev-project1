# Generated by Django 4.2.4 on 2023-09-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=300)),
                ('ayurvedic_solutions', models.CharField(max_length=300)),
            ],
        ),
    ]
