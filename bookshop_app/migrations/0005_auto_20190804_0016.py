# Generated by Django 2.2.2 on 2019-08-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0004_auto_20190803_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
