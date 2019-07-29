from django.test import TestCase

# Create your tests here.
from orm_app.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name='Peter', last_name='smith', age=23, email_address='ps@hotmail.com', marketing_consent=True)

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
