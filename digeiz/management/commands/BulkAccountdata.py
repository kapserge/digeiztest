import csv 
from time import time
from django.core.management.base import BaseCommand, CommandError

from digeiz.serializers import BulkAccountSerializer

#class Add fake test data to the API
class Command(BaseCommand):
   # help = 'Add fake test data to the API'

    def handle(self, *args, **options):
        try:
            with open('data/fake.csv','r') as fin:
                csvreader =csv.reader(fin)
                headers = next(csvreader)
                data =[{'name':row[0]
                       }
                        for row in csvreader
                      ]
                start = time()
                serializer_bulk = BulkAccountSerializer(data={'accounts': data})
                if serializer_bulk.is_valid():
                    serializer.create(data)
                stop = time()
                print(f'{len(data)} item added in {stop-start} seconds')
        
        except FileExistsError:
            raise commandError('No testdata found')

