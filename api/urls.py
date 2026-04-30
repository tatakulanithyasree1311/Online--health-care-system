from django.urls import path
from.import views
urlpatterns=[
    path('getdoctors/',views.getdoctorapi)
]