from django.conf.urls import url
from django.contrib import admin
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^devices?$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create', 'get': 'list'}), name='create_fcm_device'),
]
