import csv 
from time import time

from django.core.management.base import BaseCommand, CommandError

from digeiz.serializers import AccountSerializer

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

                for item in data:
                    serializer = AccountSerializer(data=item)
                    if serializer.is_valid():
                        serializer.create(item)
                stop = time()

                print(f'{len(data)} items added in {stop-start} seconds')

        except FileExistsError:

            raise commandError('No testdata found')

