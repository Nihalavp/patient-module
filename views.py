from django.shortcuts import render

# Create your views here.
def patient_signup(request):
    return render(request,'patient_template/signup_page.html')

def patient_login(request):
    return render(request,'patient_template/login.html')

   
def patient_appoinment(request):
    return render(request,'patient_template/appoinment.html') 

    
def patient_appoinment2(request):
    return render(request,'patient_template/appoinment2.html')    

  
    
def patient_appoi(request):
    return render(request,'patient_template/appoi.html')    

        
def patient_appoinment3(request):
    return render(request,'patient_template/appoinment3.html')    

            
def patient_appoinment4(request):
    return render(request,'patient_template/appoinment4.html')    


            
def patient_appoinmenttt(request):
    return render(request,'patient_template/appoinmenttt.html')    
