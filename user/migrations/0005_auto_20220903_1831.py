# Generated by Django 3.2.4 on 2022-09-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220903_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproduct',
            name='dprice',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myproduct',
            name='pprice',
            field=models.IntegerField(),
        ),
    ]