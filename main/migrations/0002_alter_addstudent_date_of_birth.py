# Generated by Django 4.1 on 2022-09-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='date_of_birth',
            field=models.DateField(max_length=12),
        ),
    ]
