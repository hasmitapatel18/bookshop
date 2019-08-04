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

# class Line_itemsTestCase(TestCase):
#     def setUp(self):
#         b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1")
#         be1 = Book_entry.objects.create(book=b1, price=1299, stock=10)
#         basket1=Basket.objects.create()
#         self.line_item = Line_items.objects.create(book_entry=be1, quantity=10, basket=basket1)
#
#     def test_total_price(self):
#         """check total price"""
#         self.assertEqual(self.line_item.total_price(), 12990)
#
#     def test_update_quantity(self):
#         """check update quantity method"""
#         self.line_item.update_quantity(9)
#         self.assertEqual(self.line_item.quantity, 9)
