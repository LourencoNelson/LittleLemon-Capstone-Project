from django.test import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")