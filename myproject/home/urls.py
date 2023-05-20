from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    
    path('booking', views.booking,name='booking'),
    path('doctors', views.doctors,name='doctors'),
   
    path('department', views.department,name='department'),
]