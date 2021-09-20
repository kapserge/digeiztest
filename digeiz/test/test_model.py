from django.test import TestCase
from digeiz.models import Account

class AccountModelTest(TestCase):
    @classmethod
    def setUp(cls):
        #set up non-modified objects Account by all test methods
        Account.objects.create(name='maeva')
    
    def test_name_label(self):
        account = Account.objects.get(id=1)
        field_label = account._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
    
    def test_name_max_length(self):
        account = Account.objects.get(id=1)
        max_length = Account._meta.get_field('name').max_length
        self.assertEquals(max_length, 60)
    
    