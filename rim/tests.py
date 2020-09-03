from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.urls import reverse
from rim import urls

# Create your tests here.
class TestHttpResponse(TestCase):
    def setUp(self):
        # Url dictionary to hold names for existing rim web pages, add as neccessary 
        urlDictionary = {
            "Home": reverse('home'),
            "Add": reverse('add'),
            "Edit": reverse('edit', args = [1]),
            "Client": reverse('client', args = [1]),
            "Client List": reverse('client_list')
        }
        self.urlDictionary = urlDictionary
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='', password='test')
        c = Client()
        c.login(username='test', password='test')
    


    # get_key looks up they key in urlDictionary based on the provided value
    def get_key(self, val):
        for key, value in self.urlDictionary.items():
            if val == value:
                return key

    # test_http_response iterates through the pages and checks if all pages all returning HTTP 200(OK) 
    # response, otherwise the test will be failed and the name/returned code of the faulty page will be printed to the console
    # and a ConnectionError will be raised
    def test_http_response(self):
        client = Client()
        passedFlag = True
        for url in self.urlDictionary.values():
            try:
                response = client.post(url, follow=True)
                self.assertContains(response, '', status_code=200)
            except AssertionError as e:
                passedFlag = False
                currentUrlKey = self.get_key(url)
                e = "The " + currentUrlKey + " page returned " + str(response.status_code) + " (expected 200)"
                print('\n' + e)
        if (not passedFlag):
            raise ConnectionError
#End of TestHttpResponse class
        

