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
        # self.urlDictionary = urlDictionary
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='', password='test')
        c = Client()
        self.c = c
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
        passedFlag = True
        for url in self.urlDictionary.values():
            response = self.c.get(url, follow=True)
            expected_url = url
            #SimpleTestCase().assertRedirects(response, expected_url , status_code=302, target_status_code=200, msg_prefix='ERROR', fetch_redirect_response=True)
            self.assertEqual(response.status_code, 200, 'The %s page returned %d (expected 200)' % (self.get_key(url), response.status_code))
        #     try:
        #         response = client.post(url, follow=True)
        #         self.assertContains(response, '', status_code=200)
        #     except AssertionError as e:
        #         passedFlag = False
        #         currentUrlKey = self.get_key(url)
        #         e = "The " + currentUrlKey + " page returned " + str(response.status_code) + " (expected 200)"
        #         print('\n' + e)
        # if (not passedFlag):
        #     raise ConnectionError
#End of TestHttpResponse class
        

