from django.contrib import admin

from .models import Account
from .models import Mall
from .models import Unit

admin.site.register(Account)
admin.site.register(Mall)
admin.site.register(Unit)
