from django.shortcuts import render,redirect
from . models import *
import random

# Create your views here.
def RegisterPage(request):
    return render(request,"doctor_app/authentication/register.html")

def LoginPage(request):
    return render(request,"doctor_app/authentication/login.html")

def DashboardAdmin(request):
    return render(request,"doctor_app/dashboard/index.html")

def AllDoctors(request):
    doc = Doctor.objects.all()
    return render(request,"doctor_app/doctor/doctors.html",{'doctor' : doc})

def DocProfile(request,pk):
    doctor = Doctor.objects.get(id=pk)
    return render(request,"doctor_app/doctor/profile.html",{'doc':doctor})

def PatientProfile(request):
    # patient = Patient.objects.get(id=pk)
    return render(request,"doctor_app/patients/patients-profile.html")

def RegisterData(request):
    try:
        if request.POST['role'] == "Doctor":
            role = request.POST['role']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            gender = request.POST['gender']

            user = Admin.objects.filter(Email=email)
            if user:
                msg = "User Already Exist"
                return render(request,"doctor_app/authentication/register.html",{'err':msg})
            else:
                otp = random.randint(100000, 999999)
                admin = Admin.objects.create(Email=email, Password=password, Role=role, Otp=otp)

                doctor = Doctor.objects.create(Doctor=admin,Firstname=fname,Lastname=lname, Gender=gender)
                return redirect('loginpage')

        else:
            if request.POST['role'] == "Patient":
                role = request.POST['role']
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                password = request.POST['password']
                gender = request.POST['gender']

                user = Admin.objects.filter(Email=email)
                if user:
                    msg = "User Already Exist"
                    return render(request,"doctor_app/authentication/register.html",{'err':msg})
                else:
                    otp = random.randint(100000, 999999)
                    admin = Admin.objects.create(Email=email, Password=password, Role=role, Otp=otp)

                    patient = Patient.objects.create(Patient=admin,Firstname=fname,Lastname=lname, Gender=gender)
                    return redirect('loginpage')
    except Exception as error:
        print(f"Registration error",error)

def LoginUser(request):
    if request.method == "POST":
        role = request.POST['role'] 
        email = request.POST['email']
        password = request.POST['password'] 

        user =Admin.objects.filter(Email=email, Role=role)
        if len(user)>0:

            if user[0].Password == password:
                if user[0].Role == "Doctor":
                    doc = Doctor.objects.get(Doctor=user[0])
                    request.session['id'] = user[0].id 
                    request.session['role'] = user[0].Role
                    request.session['email'] = user[0].Email
                    request.session['firstname'] = doc.Firstname
                    print(f"Doctor Session:{request.session['role']}")
                    return redirect("adminpanel")
                
                else:
                    if user[0].Role == "Patient":
                        pat =  Patient.objects.get(Patient=user[0])
                        request.session['id'] = user[0].id 
                        request.session['role'] = user[0].Role
                        request.session['email'] = user[0].Email
                        request.session['firstname'] = pat.Firstname
                        print(f"Patient Session:{request.session['role']}")
                        return redirect("adminpanel")
            else:
                msg = "Password is invalid"
                return render(request,"doctor_app/authentication/login.html",{'err':msg})

        else:
            msg = "User and role doesn't match"
            return render(request,"doctor_app/authentication/login.html")


def UpdateDoctor(request,pk):
    try:
        doctor = Doctor.objects.get(id=pk)  
        doctor.Firstname = request.POST['fname']if request.POST['fname'] else doctor.Firstname
        doctor.Lastname = request.POST['lname']if request.POST['lname'] else doctor.Lastname
        doctor.Doctor.Email = request.POST['email']if request.POST['email'] else doctor.Doctor.Email
        doctor.Doctor.Password = request.POST['password']if request.POST['password'] else doctor.Doctor.Password
        doctor.Gender = request.POST['gender']if request.POST['gender'] else doctor.Gender
        doctor.save()
        return render(request,"doctor_app/doctor/profile.html",{'doc':doctor})

    except Exception as err:
        print("Error",err)        
