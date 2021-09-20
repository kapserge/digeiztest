#views 
from .serializers import AccountSerializer, BulkAccountSerializer
from .models import Account
from rest_framework.response import Response
from .paginations import AccountPagination
from rest_framework.viewsets import ModelViewSet

class AccountView(ModelViewSet):
      queryset = Account.objects.all()
      serializer_class = AccountSerializer
      pagination_class = AccountPagination

      def create(self,request, *args, **kwargs):

          if isinstance(request.data,dict):
              return super(AccountView, self).create(request, *args, **kwargs)
          elif isinstance(request.data, list):
              serializer = BulkAccountSerializer(data={'account': request.data})
              if serializer.is_valid():
                  serializer.create(request.data)
                  return Response(serializer.data, status=201)
              else:
                  return Reponse(serializer.errors, status=400)
          else:
              return Reponse('invalid data received', status=400)

      
      