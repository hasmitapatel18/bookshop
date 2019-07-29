from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    email_address=models.EmailField()
    marketing_consent=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def revoke_marketing_consent(self):
        self.marketing_consent=False
        self.save()
        return "email notification sent"


class Address(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    house_number=models.PositiveSmallIntegerField(blank=True, null=True)
    postcode=models.PositiveIntegerField(blank=True, null=True)

    # should be a mixture of numbers and text but can't


class Payment_option(models.Model):
    Visa = "V"
    Mastercard = "MC"
    American_express = "AM"
    Pay_pal = "PP"

    card_type_choices=[(Visa, 'Visa'), (Mastercard, 'Mastercard'), (American_express, 'American_express'), (Pay_pal, 'Pay_pal')]
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    card_type=models.CharField(max_length=200, choices=card_type_choices, default='VISA')
    card_name=models.CharField(max_length=200)
    card_number=models.PositiveIntegerField(blank=True, null=True)
    expiry_date=models.DateTimeField(blank=True, null=True)
    start_date=models.DateTimeField(blank=True, null=True)
    security_cvc=models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.card_type


class Book(models.Model):
    Hardback = "HB"
    Softback = "SB"
    cover_choices = [(Hardback, 'Hardback'), (Softback, 'Softback'),]
    isbn=models.PositiveIntegerField(blank=True, null=True)
    book_name=models.CharField(max_length=200)
    cover=models.CharField(max_length=200, choices=cover_choices, default=Softback)

    def __str__(self):
        return self.book_name


class Book_entry(models.Model):
    book=models.ForeignKey(Book, default=1, on_delete = models.SET_DEFAULT)
    price=models.PositiveIntegerField(blank=True, null=True)
    # book_image=models.ImageField()
    # cloudinary
    stock=models.PositiveIntegerField(blank=True, null=True)

    # def add_to_basket():
    #
    #
    # def create_review(): ????





class Line_items(models.Model):
    book_entry=models.ForeignKey(Book_entry, default=1, on_delete = models.SET_DEFAULT)
    total_price=models.IntegerField(blank=True, null=True)
    quantity=models.IntegerField(blank=True, null=True)

    # def update_quanyity():



class Basket(models.Model):
    line_items=models.ForeignKey(Line_items, default=1, on_delete = models.SET_DEFAULT)

class Order(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    basket=models.ForeignKey(Basket, default=1, on_delete = models.SET_DEFAULT)
    payment_option=models.ForeignKey(Payment_option, default=1, on_delete = models.SET_DEFAULT)
    address=models.ForeignKey(Address, default=1, on_delete = models.SET_DEFAULT)

    # def pay():






class Review(models.Model):
    customer=models.ForeignKey(Customer, default=1, on_delete = models.SET_DEFAULT)
    book_entry=models.ForeignKey(Book_entry, default=1, on_delete = models.SET_DEFAULT)
    review=models.CharField(max_length=2000)
    rating_count=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.review



class Author(models.Model):
    book=models.ForeignKey(Book, default=1, on_delete = models.SET_DEFAULT)
    author_name=models.CharField(max_length=200)

    def __str__(self):
        return self.author_name
