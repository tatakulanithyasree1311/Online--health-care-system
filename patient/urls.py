from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insertview),
    path('record/', views.selectview, name='selectpatient'),
    path('update/<int:pid>/', views.updatepatient, name='updatepatienturl'),
    path('delete/<int:pid>/', views.deletepatient, name='deletepatienturl'),
    path('main/',views.mainview,name='mainurl'),
    path('signup/',views.signupview,name='signupurl'),
    path('login/',views.loginview,name='loginurl'),
    path('option/', views.optionview, name='optionurl'),
    path('insert/', views.insertview, name='inserturl'),
    path('doc_insert/', views.insert1, name='doctor_insert'),
    path('doc_record/', views.selectview1, name='selectpatient1'),
    ]