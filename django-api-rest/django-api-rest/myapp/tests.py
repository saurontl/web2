from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from store.models import Product


class OrderAPITest(APITestCase):
    def setUp(self):
        self.client_user = Client.objects.create(name='José')
        self.product1 = Product.objects.create(
            name="Livro", price=30.0, stock=100)
        self.product2 = Product.objects.create(
            name="Mouse", price=50.0, stock=100)

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            "client": self.client_user.id,
            "products": [self.product1.id, self.product2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)


class ProductAPITestWithAuth(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user', password='123456')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_product_authenticated(self):
        url = reverse('product-list')
        data = {
            "name": "Notebook",
            "price": "3499.90",
            "stock": 12
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Notebook")
