from django.db import models
import datetime
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.SET_DEFAULT)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    marketing_consent=models.BooleanField(default=False)

    def customer_name(self):
        full_name = self.user.get_full_name()
        return full_name

    def email(self):
        return user.email

    def revoke_marketing_consent(self):
        self.marketing_consent=False
        self.save()
        return "email notification sent"


class Address(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    house_number=models.CharField(max_length=10,blank=True, null=True)
    postcode=models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.house_number



class Payment_option(models.Model):
    Visa = "V"
    Mastercard = "MC"
    American_express = "AM"
    Pay_pal = "PP"

    card_type_choices=[(Visa, 'Visa'), (Mastercard, 'Mastercard'), (American_express, 'American_express'), (Pay_pal, 'Pay_pal')]
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    card_type=models.CharField(max_length=200, choices=card_type_choices, default='Visa')
    card_name=models.CharField(max_length=200)
    card_number=models.PositiveIntegerField(blank=True, null=True)
    expiry_date=models.DateTimeField(blank=True, null=True)
    start_date=models.DateTimeField(blank=True, null=True)
    security_cvc=models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.card_type


class Order(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)


class Basket(models.Model):
    order=models.OneToOneField(Order, primary_key=True, on_delete = models.SET_DEFAULT, default=1)


class Line_items(models.Model):
    basket=models.ForeignKey(Basket, default=1, on_delete = models.SET_DEFAULT)
    total_price=models.IntegerField(blank=True, null=True)
    quantity=models.IntegerField(blank=True, null=True)

    def total_price(self):
        amount = self.book_entry.price * self.quantity
        return amount

    def update_quantity(self, quantity):
        self.quantity=quantity
        self.save()


class Author(models.Model):
    author_name=models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    Hardback = "HB"
    Softback = "SB"
    cover_choices = [(Hardback, 'Hardback'), (Softback, 'Softback'),]
    author=models.ForeignKey(Author, default=1, on_delete = models.SET_DEFAULT)
    isbn=models.CharField(max_length=200, blank=True, null=True)
    book_name=models.CharField(max_length=200)
    cover=models.CharField(max_length=200, choices=cover_choices, default=Softback)

    def __str__(self):
        return self.book_name


class Review(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    review=models.TextField()
    rating_count=models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.review

    def reviewer_name(self):
        return "%s by"% customer.customer_name()



class Book_entry(models.Model):
    line_items=models.OneToOneField(Line_items, primary_key=True, on_delete = models.SET_DEFAULT, default=1)
    book=models.ForeignKey(Book, default=1, on_delete = models.SET_DEFAULT)
    review=models.ForeignKey(Review, default=1, on_delete = models.SET_DEFAULT)
    price=models.PositiveIntegerField(blank=True, null=True)
    stock=models.PositiveIntegerField(blank=True, null=True)

    def add_to_basket(self):
        basket = self.line_items.basket
        pass

    def create_review(self):
        review = self.review
        pass

    def if_in_stock(self):
        if self.stock > 0:
            return str(self.stock) %" available%s"
        else:
            return "not in stock"


class Book_image(models.Model):
    book_entry=models.ForeignKey(Book_entry, default=1, on_delete = models.SET_DEFAULT)
    image_book = models.ImageField(blank=True, null=True)
    image_url = models.TextField(null=True,blank=True)
