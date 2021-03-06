from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('app.api.urls', namespace='api')),
    url(r'^get-api-token/', obtain_auth_token),
]
