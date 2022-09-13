# Generated by Django 4.1 on 2022-09-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_addstudent_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudent',
            name='isTeacher',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.addstudent')),
            ],
        ),
    ]
