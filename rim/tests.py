from django.test import TestCase, Client

# Create your tests here.
class TestHttpResponse(TestCase):
    # Url dictionary to hold names for existing rim web pages, add as neccessary 
    urlDictionary = {
        "Admin Panel": '/admin/',
        "Home": '/',
        "Add": '/add/',
        "Edit": '/edit/1',
        "Client": '/client/1'
    }

    # get_key looks up they key in urlDictionary based on the provided value
    def get_key(self, val):
        for key, value in self.urlDictionary.items():
            if val == value:
                return key

    # test_http_response iterates through the pages and checks if all pages all returning HTTP 200(OK) 
    # response, otherwise the test will be failed and the name of the faulty page will be printed to the console
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
                e = "The " + currentUrlKey + " page did not return a valid HTTP 200(OK) response"
                print('\n' + e)
        if (not passedFlag):
            raise ConnectionError
#End of TestHttpResponse class
        

