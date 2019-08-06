from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import get_user_model
# Create your tests here.
from bookshop_app.models import *



class CustomerTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(first_name='peter', last_name='smith', username='petersmith', email='petersmith@hotmail.com')
        self.c1 = Customer.objects.create(user=self.u1, age=23, marketing_consent=True)

    def test_customer_name(self):
        """test customer_name method"""
        peter = Customer.objects.get(user=self.u1)
        self.assertEqual(peter.customer_name(), 'peter smith')


    def test_customer_has_email_address(self):
        """customer has email address"""
        peter = Customer.objects.get(user=self.u1)
        self.assertEqual(peter.user.email, 'petersmith@hotmail.com')

    def test_return_string(self):
        """return string- email notification"""
        peter = Customer.objects.get(user=self.u1)
        self.assertEqual(peter.revoke_marketing_consent(), 'email notification sent')

    def test_revoke_marketing_consent(self):
        """test marketing consent set to false"""
        peter = Customer.objects.get(user=self.u1)
        peter.revoke_marketing_consent()
        self.assertEqual(peter.marketing_consent, False)




class ReviewTestCase(TestCase):

    def setUp(self):
        u1 = User.objects.create_user(first_name='peter', last_name='smith', username='petersmith', email='petersmith@hotmail.com')
        peter_c = Customer.objects.create(user=u1, age=23, marketing_consent=True)
        a1 = Author.objects.create(author_name="Shakespeare")
        b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
        self.rev = Review.objects.create(customer=peter_c, book=b1)

    def test_reviewer_name(self):
        """return name of reviewer using review_name method"""
        self.assertEqual(self.rev.reviewer_name(), 'by: peter smith')



    class BookEntryTestCase(TestCase):
        def setUp(self):
            u1 = User.objects.create_user(first_name='peter', last_name='smith', username='petersmith', email='petersmith@hotmail.com')
            peter_c = Customer.objects.create(user=u1, age=23, marketing_consent=True)
            a1 = Author.objects.create(author_name="Shakespeare")
            b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
            self.be1 = Book_entry.objects.create(book=b1, price=1299, stock=10)

        def test_if_in_stock(self):
            """check if in stock method, if stock is more than 0"""
            self.assertEqual(self.be1.if_in_stock(), "10 available" )

    #     # def test_if_in_stock(self):
    #     #     """if stock=0 -is not available"""
    #     #     self.assertEqual(self.be1.if_in_stock(), "not in stock" )



class LineItemsTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create_user(first_name='peter', last_name='smith', username='petersmith', email='petersmith@hotmail.com')
        peter_c = Customer.objects.create(user=u1, age=23, marketing_consent=True)
        a1 = Author.objects.create(author_name="Shakespeare")
        b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
        be1 = Book_entry.objects.create(book=b1, price=1299, stock=10)
        r1 = Review.objects.create(customer= peter_c, book=b1)
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


class BasketTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create_user(first_name='peter', last_name='smith', username='petersmith', email='petersmith@hotmail.com')
        peter_c = Customer.objects.create(user=u1, age=23, marketing_consent=True)
        a1 = Author.objects.create(author_name="Shakespeare")
        b1= Book.objects.create(cover="Hardback", isbn="abc", book_name="book1", author = a1)
        be1 = Book_entry.objects.create(book=b1, price=1299, stock=10)
        r1 = Review.objects.create(customer= peter_c, book=b1)

        a2 = Author.objects.create(author_name="Arthur Conan Doyle")
        b2= Book.objects.create(cover="Hardback", isbn="abc", book_name="book2", author = a2)
        be2 = Book_entry.objects.create(book=b2, price=3000, stock=15)
        r2 = Review.objects.create(customer= peter_c, book=b2)

        self.customer=peter_c
        self.basket1=Basket.objects.create()
        line_item = Line_items.objects.create(book_entry=be1, quantity=2, basket=self.basket1)
        line_item2 = Line_items.objects.create(book_entry=be2, quantity=1, basket=self.basket1)

    def test_create_order(self):
        """check order created"""
        self.basket1.purchase(self.customer)
        self.assertIsNotNone(self.basket1.order)

    def test_line_items_found(self):
        """check line_items_found from order"""
        self.basket1.purchase(self.customer)
        order=self.basket1.order
        # import pdb
        # pdb.set_trace()
        # we use <model_name>_set to reverse back through the fk (if not specified)
        self.assertEqual(order.basket_set.first().line_items_set.count(), 2)
