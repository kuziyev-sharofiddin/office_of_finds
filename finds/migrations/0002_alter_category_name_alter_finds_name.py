# Generated by Django 4.1.5 on 2023-02-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
