from django.test import TestCase, Client
from django.urls import reverse
from events import views
from events.models import Event


class CreateEventViewTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_get_request_display_form(self):

        response = self.client.post(reverse('create_event'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create-event.html')


    def test_create_event_page_redirects(self):
        
        data = {
            'name': 'March event',
            'description': '... some random description',
            'start_date': '2023-10-01 12:00:00',
            'end_date': '2023-10-01 14:00:00',
            'location': 'Test Location',
            'location_tips': 'Test Tips',
            'call_for_direction': 'Test Direction',
            'country': 'nigeria',
            'event_type': 'business',
            'is_free': True
        }

        response = self.client.post(reverse('create_event'), data)
        self.assertEqual(response.status_code, 302)