from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUpTest(TestCase):
    user_name = 'myusername'
    email = 'myusername@gmail.com'
    
    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    
    def test_signup_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.user_name,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.user_name)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        
