# Generated by Django 3.2.8 on 2021-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='regdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
