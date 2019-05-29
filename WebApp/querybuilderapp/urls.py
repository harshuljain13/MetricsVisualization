from django.urls import path
from django.conf.urls import url
from querybuilderapp import views

urlpatterns = [
    path('', views.home, name='qbhome',),
    url('^getschemadetails$', views.get_schema_details, name='getschemadetails'),
    url('^get_query_data$', views.get_query_data, name='get_query_data'),
]