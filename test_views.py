from django.http import HttpRequest
from django.test import TestCase, SimpleTestCase
from django.test import Client
from rim.models import Client as ClientModel
from rim.models import Checkout
from rim.views import CheckoutView, ClientView, HomeView, ListClientView, PaginateMixin
from django.urls import reverse
from rim import urls
from rim import views
from django.views.generic import ListView
from django.test.client import RequestFactory


class HomePageViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'rim/home.html')



class AddPageViewTests(TestCase):

    def test_add_page_status_code(self):
        response = self.client.get('/add/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'rim/edit.html')


class CheckoutPageViewTests(TestCase):

    def test_checkout_page_status_code(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'rim/checkout.html')



class ClientViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.sample = ClientModel.objects.create(name = "Rodney Brown", bpn = "M99456529", note = "This is a note")
       
#TODO: test 


class ClientsPageViewTests(TestCase):

    def test_clients_page_status_code(self):
        response = self.client.get('/client/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('client_list'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('client_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'rim/client_list.html')