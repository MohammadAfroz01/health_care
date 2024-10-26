from django.contrib import admin
from appointment.models import List
from appointment.models import Department
from appointment.models import DoctorDetail
from appointment.models import Contact
# Register your models here.

class List_Details(admin.ModelAdmin):
    list_display=("Departments","Doctors","date","time","full_name","Phone","message")

admin.site.register(List,List_Details)    

#Department 
class DepartmentAdmin(admin.ModelAdmin):
    list_display=("department_name","department_description")


class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display=("department_name","doctor_full_name","gender","age","education_status","work_experience","email_id","mobile_number","doctor_description","avialiable_work_hours","state","city","image")

class ContactAdmin(admin.ModelAdmin):
    list_display=("Full_name","Email_id","Query","Ph_number","Message")

    
admin.site.register(Department,DepartmentAdmin)   
admin.site.register(DoctorDetail,DoctorDetailsAdmin)
admin.site.register(Contact, ContactAdmin)