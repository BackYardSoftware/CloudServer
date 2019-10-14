from django.contrib import admin
from django.urls import path, include
from devices import views as devices
from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    

    # add device
    path('Add_device/', devices.device_add, name='Add_device'),
    path('Devices_list/', devices.device_list, name='device_list'),

    path('accounts/', include('django.contrib.auth.urls')),

    # django admin page
    path('admin/', admin.site.urls),
]
