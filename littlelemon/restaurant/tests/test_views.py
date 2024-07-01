from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(name='Menu 1', description='Descripción 1')
        self.menu2 = Menu.objects.create(name='Menu 2', description='Descripción 2')

    def test_getall(self):
        response = self.client.get('/menus/')

        menus = Menu.objects.all()
        expected_data = {'menus': [{'name': menu.name, 'description': menu.description} for menu in menus]}

        self.assertEqual(response.data, expected_data)