from django.test import TestCase
from django.urls import reverse
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Pangalactic Gargleblaster', price = 42.42, inventory=1)
        Menu.objects.create(title='Expensive Salad', price = 27.19, inventory=17)
        Menu.objects.create(title='Cheap Whiskey', price = 21.42, inventory=19)
        Menu.objects.create(title='Expensive Bread', price = 16.32, inventory=10)

    def test_getall(self):
        menuItems = Menu.objects.all().order_by('-id')
        serialized_q = MenuSerializer(menuItems, many=True)
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.data['results'], serialized_q.data)