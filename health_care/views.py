
from django.http import HttpResponse ,HttpResponseRedirect,JsonResponse
from django.shortcuts import render ,redirect
from appointment.models import List , Department , DoctorDetail ,Contact
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages import get_messages

def homePage(request):
    all_depart=Department.objects.all()
    if request.method =="POST":

        department = request.POST["departments"]
        doctor = request.POST["department_doctor_name"]
        dates = request.POST["Date"]
        time = request.POST["Time"]
        name = request.POST["full_name"]
        number = request.POST["phone"]
        msg = request.POST["message"]
        data=List(Departments=department,Doctors=doctor,date=dates,time=time,full_name=name,Phone=number,message=msg)
        data.save()

        return redirect("confirmation")
    return render(request,"index.html",{"all_depart":all_depart})

def get_doctor_department_name_ajax(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        # print(subject_id)
        try:
                # subject = Subject.objects.filter(id = subject_id).first()
                department_details=Department.objects.filter(department_name=subject_id).values()
                # print(department_details)
                # print(department_details[0]['id'])
                topics = DoctorDetail.objects.filter(department_name = department_details[0]['id'])
                # print(topics)
        except Exception:
                data={}
                data['error_message'] = 'error'
                return JsonResponse(data)
        return JsonResponse(list(topics.values('id', 'department_name','doctor_full_name')), safe = False) 
    return render(request,"index.html")    

def aboutPage(request):
    return render(request,"about.html")

def servicePage(request):
      doctor_details=Department.objects.all()
    
      return render(request,"service.html",{"doctor_details":doctor_details})

def allDoctorPage(request,id):
    all_doctors=DoctorDetail.objects.filter(department_name_id=id)

    return render(request,"all-doctors.html",{"all_doctors":all_doctors})

def SingleDoctorDetailsPage(request,id):
    Single_doctors=DoctorDetail.objects.get(id=id)
    return render(request,"doctor-details.html",{"Single_doctors":Single_doctors})

def departmentPage(request):
    return render(request,"department.html")

def departmentsinglePage(request):
    return render(request,"department-single.html")

def doctorPage(request):
    Doctors=DoctorDetail.objects.all()

    return render(request,"doctor.html",{"Doctors":Doctors})

def doctorsinglePage(request):
    return render(request,"doctor-single.html")

def blogsidebarPage(request):
    return render(request,"blog-sidebar.html")

def blogsinglePage(request):
    return render(request,"blog-single.html")

def appointmentPage(request,id):
    my_list=[]
    msg=''
    Doctor_detail = None
    if id is not None:
      Doctor_detail=DoctorDetail.objects.filter(id=id).values()
    if Doctor_detail:
      dict1={}
      dict1['doc_name']=Doctor_detail[0]['doctor_full_name']
    
      doc_department_id=Doctor_detail[0]['department_name_id']
      Deparment_details=Department.objects.filter(id=doc_department_id).values()

      dict1['department_name']=Deparment_details[0]['department_name']
    
      my_list.append(dict1)
      print(my_list)
      
    # my_list=[doc_name,department_name]
    
    if request.method =="POST":
    

        department = request.POST.get("Departments", '')
        doctor = request.POST.get("Doctors", '')  
        dates = request.POST.get("Date", '')  
        time = request.POST.get("Time", '')  
        name = request.POST.get("full_name", '') 
        number = request.POST.get("Phone", '') 
        msg = request.POST.get("message", '')  
         
        data = List(Departments=department, Doctors=doctor, date=dates, time=time, full_name=name, Phone=number, message=msg)
        data.save()
            
        return redirect("confirmation")
    
    
        
    return render(request,"appointment.html",{'my_list':my_list,"Doctor_detail":Doctor_detail ,'id':id,})


def confirmationPage(request):

    return render(request,"confirmation.html")


def contactPage(request):

    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        query_topic = request.POST.get('subject')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')

        # Validate the form fields
        if not full_name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return render(request, "contact.html", {
                'full_name': full_name,
                'email': email,
                'query_topic': query_topic,
                'phone_number': phone_number,
                'message': message
            })

        contact = Contact(
            Full_name=full_name,
            Email_id=email,
            Query=query_topic,
            Ph_number=phone_number,
            Message=message
        )
        contact.save()
        print("Redirecting to feedback page...")
        return redirect("Feedback")

    return render(request, "contact.html")


def feedbackpage (request):

    return render(request,"feedback.html")