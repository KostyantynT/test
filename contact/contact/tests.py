from django.test import Client
from django.test import TestCase
from django.core.management import call_command
from django.core.urlresolvers import reverse
from StringIO import StringIO

from models import ContactInfo
from models import RequestLog
from models import HistoryLog


class ContactViewTest(TestCase):
    fixtures = ['initial_data.json']

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
        #check that page actually has necessary data
        for f in db_contact._meta.get_all_field_names():
            if f != 'birthdate':
                self.assertContains(response, db_contact.__getattribute__(f))
        #check that we have admin edit link in the view
        #we should be logged in
        res = c.login(username='admin', password='admin')
        self.assertTrue(res)
        response = c.get(url)
        self.assertContains(response, "(admin)")


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

        #check that data has correct ordering
        first_date = requests_list[0].time
        for r in requests_list:
            self.assertGreaterEqual(r.time, first_date)
            first_date = r.time


class ContextProcessorTest(TestCase):
    def test_context_processor(self):
        #make some request and check if response.context contains our settings
        url = reverse("requests_view")
        c = Client()
        result = c.get(url)
        self.assertTrue('settings' in result.context)


class EditFormTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        pk = ContactInfo.objects.all()[0].pk
        self.url = reverse('contact_edit', kwargs={'pk': pk})

    def test_edit_form(self):
        #make sure edit form exist
        c = Client()
        result = c.get(self.url)

        #it should be available after login...
        self.assertEqual(result.status_code, 302)

        result = c.login(username='admin', password='admin')
        self.assertTrue(result, 'Login was unsuccessful')
        #now we should get correct response
        result = c.get(self.url)
        self.assertEqual(result.status_code, 200)

        #we should had object to change
        ci = ContactInfo.objects.all()[0]

        self.assertFalse(ci is None, 'ContactInfo is None')

        #we will try to save the wrong data
        contactinfo = {}
        ci.email = "testcom"
        for field in ci._meta.get_all_field_names():
            contactinfo[field] = ci.__getattribute__(field)

        del contactinfo['photo']

        result = c.post(self.url, contactinfo, follow=True)
        self.assertContains(result, 'Enter a valid email address.')

        contactinfo['birthdate'] = '27/08/1982 16:55'

        contactinfo['email'] = "tset@test.com"
        result = c.post(self.url, contactinfo, follow=True)
        self.assertRedirects(result, reverse('contact_view'))
        #we should be redirected
        self.assertEqual(result.status_code, 200)
        #view should contain new email
        self.assertContains(result, contactinfo['email'])


class CommandTest(TestCase):
    fixtures = ['initial_data.json']

    def test_print_models_command(self):
        o = StringIO()
        e = StringIO()
        call_command('printmodels', stdout=o, stderr=e)
        self.assertTrue('ContactInfo model has 1 object(s).' in o.getvalue())
        self.assertTrue('error: ContactInfo model has 1 object(s).' in e.getvalue())


class SignalsTest(TestCase):
    fixtures = ['initial_data.json']

    def test_signals_are_stored(self):
        #required for registering signals...
        from contact import signals
        #make sure we have empty logs
        obj = HistoryLog.objects.all()
        self.assertEqual(len(obj), 0)
        #let's update one record
        ci = ContactInfo.objects.all()[0]
        ci.name = 'New name'
        ci.save()
        #make sure we have one update record
        obj = HistoryLog.objects.all()
        self.assertEqual(len(obj), 1)
        updaterecord = obj[0]
        self.assertEqual(updaterecord.action, 'U')
        #let's delete the record
        ci.delete()
        obj = HistoryLog.objects.get(action='D')

        #let's check that model name equal ContactInfo
        self.assertEqual(obj.objectModel, 'ContactInfo')
        self.assertEqual(obj.action, 'D')
