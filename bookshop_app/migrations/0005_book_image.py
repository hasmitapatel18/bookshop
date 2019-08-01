# Generated by Django 2.2.2 on 2019-07-30 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0004_auto_20190730_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_book', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.TextField(blank=True, null=True)),
                ('book_entry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Book_entry')),
            ],
        ),
    ]