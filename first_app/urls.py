from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('services/',views.services, name='services')
]
