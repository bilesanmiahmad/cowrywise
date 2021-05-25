from django.http import response
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import DataModel

# Create your tests here.
class DataModelTestCase(TestCase):
    def setUp(self):
        uid = "610a7063-a789-4e87-8491-ba4efdb331c1"
        DataModel.objects.create(uuid=uid)

    def test_entity_type_string_representation(self):
        data = DataModel.objects.get(uuid="610a7063-a789-4e87-8491-ba4efdb331c1")
        self.assertEqual(str(data), "610a7063-a789-4e87-8491-ba4efdb331c1")

class DataModelTests(APITestCase):

    def test_valid_datamodel_endpoint(self):
        url = reverse("data-list")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)