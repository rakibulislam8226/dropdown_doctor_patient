
from django.contrib import admin
from django.urls import path
from dropdown_doctor_patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/add/', views.create_view, name='add'),
    path('patient/ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'),
]
