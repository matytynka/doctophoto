from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('examination/<int:exam_id>', views.examination, name='examination'),

    path('account/login/patient', views.login_patient, name='login'),
    path('account/login/doctor', views.login_doctor, name='logout'),
    path('account/logout', views.logout),
    path('signup', views.signup, name='signup')
]
