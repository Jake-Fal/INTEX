# Generated by Django 4.1.2 on 2022-11-30 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_fooditem_foodname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='fdic',
        ),
    ]
