# Generated by Django 3.2.8 on 2021-12-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0002_alter_customer_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='currentreading',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='previousreading',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
