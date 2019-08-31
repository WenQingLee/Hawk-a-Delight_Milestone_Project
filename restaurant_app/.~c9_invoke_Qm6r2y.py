from django.test import TestCase
from .models import MenuItem

# Create your tests here.

# Tests for MenuItem model
class MenuItemTests(TestCase):
    
    def setUp(self):
        MenuItem.objects.create(name='Chicken Rice', description='This is chicken rice.', price=2.10)
    
    # Testing the name, description and price fields for the MenuItem model
    def test_MenuItemFields(self):
        test = MenuItem.objects.get(name='Chicken Rice')
        self.assertEqual(test.name, 'Chicken Rice')
        self.assertEqual(test.description, 'This is chicken rice.')
        self.assertEqual(str(test.price), '2.10')
        