from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('Add_device/', views.Add_device, name='Add_device'),
    path('Device_list/', views.Device_list.as_view(), name='Device_list'),
    path('Data_list/', views.Data_list, name='Data_list'),
    path('Key_manager/', views.Key_manager.as_view(), name='Key_manager'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
