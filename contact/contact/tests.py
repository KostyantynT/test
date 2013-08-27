from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse

from contact.contact.models import ContactInfo

class ContactViewTest(TestCase):
    #
    def test_(self):
        url = reverse("contact_view")
        c = Client()
        response = c.get(url)
        #check that url configured
        self.assertEqual(200, response.status_code)
        
        #check that responce.context contains ContactInfo object
        self.assertIn('contact', response.context)
        
        contact = response.context['contact']
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
