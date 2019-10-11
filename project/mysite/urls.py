from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('Home/', views.Home, name='Home'),
    path('Add_device/', views.Add_device, name='Add_device'),
    path('Devices_data/', views.Devices_data, name='Devices_data'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
