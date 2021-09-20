#models.py
from django.db import models

class Account (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def get_account(self):
        return self.name 

    def __str__(self):
        return (str(self.pk)+"_"+self.name)
    def get_absolute_url(self):
        return reverse('account-detail', args=[str(self.id)])

class Mall (models.Model):

    name = models.CharField(max_length=60)
    Account_Id = models.ForeignKey(Account, related_name ='mall_account', on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name


class Unit (models.Model):

    name = models.CharField(max_length=60)
    Mall_Id = models.ForeignKey(Mall, related_name ='unit_mall', on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name
