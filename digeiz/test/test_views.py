from django.test import TestCase
from django.urls import reverse

from digeiz.models import Account

class AccountListViewTest(TestCase):
    @classmethod
    #Create 10 Account 
    def setUpTestData(cls):
        number_of_account = 10
        for account_id in range(number_of_account):
            Account.objects.create(name =f'christain {account_id}')
    
    def test_view_url_exists(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code,200)
    