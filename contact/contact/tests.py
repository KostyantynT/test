from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import ContactInfo
from .models import RequestLog

class ContactViewTest(TestCase):
    fixtures=['initial_data.json']
    def test_check_contactInfo_page_and_model(self):
        url = reverse("contact_view")
        #self.assertTrue(False, url)
        c = Client()
        response = c.get(url)
        #check that url configured
        self.assertEqual(200, response.status_code)
        
        #check that responce.context contains ContactInfo object
        self.assertIn('contactinfo', response.context)
        
        contact = response.context['contactinfo']
        db_contact = ContactInfo.objects.all()[0]
        #check that the first model is equal to our context variable
        self.assertEqual(contact, db_contact) 
        
        #check that html contains necessry fields from mockup template
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'Date of birth')
        self.assertContains(response, 'Bio')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Jabber')
        self.assertContains(response, 'Skype')
        self.assertContains(response, 'Other contacts')
        
        
class MiddlewareTest(TestCase):
    fixtures = ["initial_data.json"]
    def test_middle_case(self):
        #check that we don't have any entity in the database
        requests = RequestLog.objects.all()
        self.assertEqual(len(requests), 0)

        #make the http request
        url = reverse("contact_view")
        c = Client()
        contact_result_view = c.get(url)
        
        requests = RequestLog.objects.all()
        #check that database has only 1 request
        self.assertEqual(len(requests), 1)
        
        #check that database has exactly our request
        self.assertEqual(url, requests[0].path)
        
        #check that wrong request also logged
        result = c.get("some-wrong-request")
        self.assertEqual(result.status_code, 404)
        
        requests = RequestLog.objects.all()
        self.assertEqual(len(requests), 2) 
        
        url = reverse("requests_view")
        #check that contact_view has link to requests page
        self.assertContains(contact_result_view, 'requests')
        self.assertContains(contact_result_view, url)
        
        #check that we have view for requests page
        result = c.get(url)
        self.assertEqual(result.status_code, 200)
        
        #view context should contain 3 objects
        requests_list = result.context['object_list']
        self.assertEqual(len(requests_list), 3)
        #view should display path for each of object 
        for r in requests_list:
            self.assertContains(result, r.path)