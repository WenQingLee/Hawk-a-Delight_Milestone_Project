from django.test import TestCase
from .models import Order, OrderLineItem
from restaurant_app.models import MenuItem

# Create your tests here.

# Tests for Order model
class OrderTests(TestCase):
    
    def setUp(self):
        Order.objects.create(full_name='test_name', phone_number='12345678', country='Singapore', postcode='123456', town_or_city='Singapore', street_address1='Building123', date='2011-11-12')
        
    def test_OrderTests(self):
        test=Order.objects.get(full_name="test_name")
        self.assertEqual(test.full_name, "test_name")
        self.assertEqual(test.phone_number, "12345678")
        self.assertEqual(test.country, "Singapore")
        self.assertEqual(test.postcode, "123456")
        self.assertEqual(test.town_or_city, "Singapore")
        self.assertEqual(test.street_address1, "Building123")
        

# Tests for OrderLineItem model
class OrderLineItemTests(TestCase):
    def setUp(self):
        order_test = Order.objects.create(full_name='test_name', phone_number='12345678', country='Singapore', postcode='123456', town_or_city='Singapore', street_address1='Building123', date='2011-11-12')
        menu_test = MenuItem.objects.create(name='Chicken Rice', description='This is chicken rice.', price=2.10)
        OrderLineItem.objects.create(order=order_test, item=menu_test, quantity='2')
        
    def test_OrderLineItemTests(self):
        test=OrderLineItem.objects.get(quantity='2')