# Generated by Django 3.1.1 on 2022-12-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('Employee_Name', models.CharField(max_length=100)),
                ('Employee_Age', models.IntegerField()),
                ('Employee_Email', models.EmailField(max_length=254)),
                ('Employee_post', models.CharField(max_length=100)),
            ],
        ),
    ]
