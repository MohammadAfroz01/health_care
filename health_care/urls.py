"""
URL configuration for health_care project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from health_care import views
from  .views import appointmentPage,confirmationPage 
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('about-us',views.aboutPage),
    path('Service',views.servicePage),
    path('Department',views.departmentPage),
    path('Department-single',views.departmentsinglePage),
    path('Doctor',views.doctorPage),
    path('Doctor-single',views.doctorsinglePage),
    path('Appointment/<int:id>/', views.appointmentPage, name='AppointmentDetail'),
    path('Confirmation/', RedirectView.as_view(url='/ConfirmationPage/'),name='Confirmation'),
    path('ConfirmationPage/',confirmationPage , name="confirmation"),
    path('Blog-side-bar',views.blogsidebarPage),
    path('Blog-single',views.blogsinglePage),
    path('Contact/',views.contactPage , name="contact"),
    path('Feedback/',views.feedbackpage , name="Feedback"),
    path('all-doctor/<int:id>',views.allDoctorPage ,name='all-doctor'),
    path('Doctor-details/<int:id>',views.SingleDoctorDetailsPage),
    path('get-doctor-department-name-ajax/', views.get_doctor_department_name_ajax,name="get_doctor_department_name_ajax"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)