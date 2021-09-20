from rest_framework import routers
from django.urls import path, include
from .views import AccountView

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'accounts', AccountView, basename='accounts')
urlpatterns = router.urls
