from django.test import TestCase

# Create your tests here.
from bookshop_app.models import *

class CustomerTestCase(TestCase):

    def setUp(self):
        self.c = Customer.objects.create(first_name='peter', last_name='smith', username='psmith', password='foo', age=23, email_address='ps@hotmail.com', marketing_consent=True)

    def test_customer_has_email_address(self):
        """customer has email address"""
        peter = Customer.objects.get(email_address="ps@hotmail.com")
        self.assertEqual(peter.email_address, 'ps@hotmail.com')

    def test_return_string(self):
        """return string a"""
        peter = Customer.objects.get(email_address="ps@hotmail.com")
        self.assertEqual(peter.revoke_marketing_consent(), 'email notification sent')

    def test_revoke_marketing_consent(self):
        """return string a"""
        peter = Customer.objects.get(email_address="ps@hotmail.com")
        peter.revoke_marketing_consent()
        self.assertEqual(peter.marketing_consent, False)


class ReviewTestCase(TestCase):

    def setUp(self):
        peter_c = Customer.objects.create(first_name='peter', last_name='smith', username='psmith', password='foo', age=23, email_address='ps@hotmail.com', marketing_consent=True)
        self.rev = Review.objects.create(customer=peter_c)

    def test_reviewer_name(self):
        """return name of reviewer using review_name method"""
        self.assertEqual(self.rev.reviewer_name(), 'by: psmith')


class BookentryTestCase(TestCase):
    def setUp(self):
        peter_c = Customer.objects.create(first_name='peter', last_name='smith', username='psmith', password='foo', age=23, email_address='ps@hotmail.com', marketing_consent=True)
        a1 = Author.objects.create(author_name="Shakespeare")
        r1 = Review.objects.create(customer= peter_c)
        b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
        self.be1 = Book_entry.objects.create(review= r1, book=b1, price=1299, stock=10)

    def test_if_in_stock(self):
        """check if in stock method, if stock is more than 0"""
        self.assertEqual(self.be1.if_in_stock(), "10 available" )

    # def test_if_in_stock(self):
    #     """if stock is not available"""
    #     self.assertEqual(self.be1.if_in_stock(), "not in stock" )


class Line_itemsTestCase(TestCase):
    def setUp(self):
        peter_c = Customer.objects.create(first_name='peter', last_name='smith', username='psmith', password='foo', age=23, email_address='ps@hotmail.com', marketing_consent=True)
        a1 = Author.objects.create(author_name="Shakespeare")
        r1 = Review.objects.create(customer= peter_c)
        b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
        be1 = Book_entry.objects.create(review= r1, book=b1, price=1299, stock=10)
        o1=Order.objects.create(customer=peter_c)
        basket1=Basket.objects.create(order=o1)
        self.line_item = Line_items.objects.create(book_entry=be1, quantity=10, basket=basket1)


    def test_total_price(self):
        """check total price"""
        self.assertEqual(self.line_item.total_price(), 12990)

    def test_update_quantity(self):
        """check update quantity method"""
        self.line_item.update_quantity(9)
        self.assertEqual(self.line_item.quantity, 9)
