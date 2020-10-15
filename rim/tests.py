from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from django.contrib.auth.models import AnonymousUser, User
from django.urls import reverse
from rim import urls

# Create your tests here.
class TestHttpResponse(TestCase):
    fixtures = ['dummydb.json']
    def setUp(self):
        
        # Url dictionary to hold names for existing rim web pages, add as neccessary 
        self.urlDictionary = {
            "Home": reverse('home'),
            "Add": reverse('add'),
            "Edit": reverse('edit', args = [1]),
            "Client": reverse('client', args = [1]),
            "Client List": reverse('client_list')
        }
        
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='', password='test')
        self.client.login(username='test', password='test')

    # test_http_response iterates through the pages and checks if all pages all returning HTTP 200(OK) 
    # response. If the test doesn't pass it returns the name, address, and response code of the page that returned it.
    def test_http_response(self):
        for name, url in self.urlDictionary.items():
            response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, 200, 'The %s page at %s returned %d (expected 200)' % (name, url, response.status_code))
#End of TestHttpResponse class
        

