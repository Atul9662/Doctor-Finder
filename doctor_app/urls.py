from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
# PAGE URLS
    path("register-page/",views.RegisterPage,name="registerpage"),
    path("login-page/",views.LoginPage,name="loginpage"),
    path("Admin-panel/",views.DashboardAdmin,name="adminpanel"),
    path("all-doctors/",views.AllDoctors,name="alldoctors"),
    path("doctor-profile/<int:pk>/",views.DocProfile,name="doctorprofile"),
    path("patient-profile/",views.PatientProfile,name="patientprofile"),

#FUNCTIONALITIES URLS
    path ("register-data/",views.RegisterData,name="registerdata"),
    path ("login-user/",views.LoginUser, name="loginuser"),
    path ("update-doc/<int:pk>/",views.UpdateDoctor,name="updatedoc"),

    
    ]
