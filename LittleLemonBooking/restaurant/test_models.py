from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_add_new_menu(self):
        item = Menu.objects.create(title="Bok Choy Salad", price=11.55, inventory=42)
        self.assertEqual(item.__str__(), 'Bok Choy Salad : 11.55')   

