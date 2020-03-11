from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rim.urls'), name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]
