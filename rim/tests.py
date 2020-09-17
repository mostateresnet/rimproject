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
        self.c = Client()
        self.c.login(username='test', password='test')


    # get_key looks up they key in urlDictionary based on the provided value
    def get_key(self, val):
        for key, value in self.urlDictionary.items():
            if val == value:
                return key

    # test_http_response iterates through the pages and checks if all pages all returning HTTP 200(OK) 
    # response. If the test doesn't pass it returns the response code and the name of the page that returned it.
    def test_http_response(self):
        passedFlag = True
        for url in self.urlDictionary.values():
            response = self.c.get(url, follow=True)
            expected_url = url
            self.assertEqual(response.status_code, 200, 'The %s page returned %d (expected 200)' % (self.get_key(url), response.status_code))
#End of TestHttpResponse class
        

