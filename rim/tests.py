from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from django.contrib.auth.models import AnonymousUser, User
from django.urls import reverse
from rim import urls
from .forms import *
from .models import *

# Create your tests here.
class Setup(TestCase):
    fixtures = ['dummydb.json']
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='test')
        self.user.set_password('test')
        self.user.save()
        login = self.client.login(username='test', password='test')
        self.assertTrue(login) 
        

class TestHttpResponse(TestCase): 
    # test_http_response iterates through the pages and checks if all pages all returning HTTP 200(OK) 
    # response. If the test doesn't pass it returns the name, address, and response code of the page that returned it.
    def test_http_response(self):
        Setup.setUp(self)
        # Url dictionary to hold names and addresses for existing rim web pages, add as neccessary 
        self.urlDictionary = {
            "Home": reverse('home'),
            "Add": reverse('add'),
            "Edit": reverse('edit', args = [1]),
            "Client": reverse('client', args = [1]),
            "Client List": reverse('client_list')
        }
        
        for name, url in self.urlDictionary.items():
            response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, 200, 'The %s page at %s returned %d (expected 200) ' % (name, url, response.status_code))
#End of TestHttpResponse class
        
# class TestAddPage(TestCase):
#     fixture = Setup.fixtures
#     def test_AddForm_valid(self):
#         add_page = reverse('add')
#         valid_form_data = {"serial_no":"A999", "hostname":"host123", "equipment_model":"model123","equipment_type":"Laptop","count":"1",
#                         "manufacturer":"manufact" }
    
#         form = EquipmentForm(data={"serial_no":"A999", "equipment_model":"model123", "equipment_type": '1'})
#         print(form)
#         #self.assertTrue(form.is_valid())