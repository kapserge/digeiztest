#serializes.py
from rest_framework import serializers
from rest_framework.response import Response
from .models import Account
#
class AccountSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Account
        fields = ['id','name']
    
    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    

#Bulk insertion (insertion multiple)
class BulkAccountSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True)
    class Meta:
        model = Account
        fields = ['accounts'] 
    def create(self, validated_data):
        #
        create_list_objects = []
        for data in validated_data:
            #
            create_list_objects.apprend(data)
        return Account.objects.bulk_create(create_list_objects)