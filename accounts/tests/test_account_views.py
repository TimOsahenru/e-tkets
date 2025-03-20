from django.test import TestCase, Client
from django.urls import reverse
from accounts import views
from django.contrib.auth.models import User


class TestSignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()




    def test_register_get_request(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)


    def test_register_post_request_with_valid_data(self):

        data = {
            'username': 'admin',
            'email': 'adminuser@gmail.com',
            'password': 'bankuSlayer2',
            'password2': 'bankuSlayer2',
        }
        
        # response = self.client.post('register', data=data)
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.url, reverse('profile'))
        self.assertEqual(response.url, reverse('login'))
        self.assertTrue(User.objects.filter(username='admin').exists())


    def test_regular_post_request_with_invalid_data(self):
        data = {
            'username': 'admin',
            'email': 'invalid_email',
            'password': '1234',
            'password2': '1234',
        }

        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user_form'].is_valid())
        self.assertFalse(User.objects.filter(email='invali_email').exists())
