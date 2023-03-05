from django.test import TestCase, Client
from django.urls import reverse
from store.models import Profile
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        user = User.objects.create(username='sda')
        user.set_password('12345')
        user.save()

        self.profile = Profile.objects.create(
            user=user,
            street='1.avenue',
            number='5',
            post_code='00-000',
            city='N.Y',
            phone_number=2222,
            info='')

    def test_user_update_prifile(self):
        self.client.login(username='sda', password="12345")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/profile.html')