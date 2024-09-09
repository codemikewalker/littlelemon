from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(ID=1, title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.title, "IceCream")
