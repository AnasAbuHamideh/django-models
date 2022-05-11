from urllib import request, response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snacks-list")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snacks-list")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")