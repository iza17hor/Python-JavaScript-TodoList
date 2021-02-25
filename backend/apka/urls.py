from django.urls import path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('apka', DniViewSet) 
router.register('cele',CeleViewSet)


urlpatterns = router.urls

