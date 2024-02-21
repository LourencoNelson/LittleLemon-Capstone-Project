from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Booking, Menu
from Restaurant.views import MenuItemView
from Restaurant.serializers import MenuSerializer
from rest_framework import status
import json

class MenuViewTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Matapa", price=40, inventory=50)
        Menu.objects.create(title="Grilled Chicken", price=100, inventory=100)
        
        
    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
        
        self.assertEqual(response.json(), serialized_data)