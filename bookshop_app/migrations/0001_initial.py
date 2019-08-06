# Generated by Django 2.2.2 on 2019-08-06 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, max_length=200, null=True)),
                ('book_name', models.CharField(max_length=200)),
                ('cover', models.CharField(choices=[('HB', 'Hardback'), ('SB', 'Softback')], default='SB', max_length=200)),
                ('synopsis', models.TextField(default=1)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Book_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('stock', models.PositiveIntegerField(blank=True, null=True)),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('marketing_consent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('order', models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, serialize=False, to='bookshop_app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating_count', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('book_entry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Book_entry')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('V', 'Visa'), ('MC', 'Mastercard'), ('AM', 'American_express'), ('PP', 'Pay_pal')], default='Visa', max_length=200)),
                ('card_name', models.CharField(max_length=200)),
                ('card_number', models.PositiveIntegerField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('security_cvc', models.PositiveIntegerField(blank=True, null=True)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Book_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_book', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.TextField(blank=True, null=True)),
                ('book_entry', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Book_entry')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Line_items',
            fields=[
                ('book_entry', models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, serialize=False, to='bookshop_app.Book_entry')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('basket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='bookshop_app.Basket')),
            ],
        ),
    ]
