from django.urls import path
from .import views

app_name = 'patient'

urlpatterns=[
    path('signup',views.patient_signup, name="signup"),
    path('login',views.patient_login, name="login"),
    path('appoinment',views.patient_appoinment, name="appoinment"),
    path('appoinment2',views.patient_appoinment2, name="appoinment2"),
    
    path('appoinment3',views.patient_appoinment3, name="appoinment3"),
    path('appoinment4',views.patient_appoinment4, name="appoinment4"),
   


]
    


