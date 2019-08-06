from django.contrib import admin
from django.contrib.auth.models import User

from .models import *



class CustomerAdmin(admin.ModelAdmin):
    fields = [("user", "age", "marketing_consent")]


class AddressAdmin(admin.ModelAdmin):
    fields = [("customer", "house_number", "postcode")]


class Payment_optionAdmin(admin.ModelAdmin):
    fields = [("customer", "card_type", "card_name", "card_number", "expiry_date", "start_date", "security_cvc")]


class AuthorAdmin(admin.ModelAdmin):
    fields = [("author_name")]


class BookAdmin(admin.ModelAdmin):
    fields = [("author", "isbn", "book_name", "cover", "synopsis")]


class Book_entryAdmin(admin.ModelAdmin):
    fields = [("book", "price", "stock")]


class ReviewAdmin(admin.ModelAdmin):
    fields = [("customer", "book_entry", "review", "rating_count", "timestamp")]


class Book_imageAdmin(admin.ModelAdmin):
    fields = [("book_entry", "image_book")]


class OrderAdmin(admin.ModelAdmin):
    fields = [("customer")]


class BasketAdmin(admin.ModelAdmin):
    fields = [("order")]


class Line_itemsAdmin(admin.ModelAdmin):
    fields = [("book_entry", "Basket", "total_price", "quantity")]



admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Payment_option)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Book_entry)
admin.site.register(Review)
admin.site.register(Book_image)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(Line_items)
