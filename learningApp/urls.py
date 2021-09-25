from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
            
    path('about', views.about, name='about'),
    path('addCourse', views.addCourse, name='addCourse'),
    path('courses', views.courses, name='courses'),


    path('login', views.handelLogin, name='login'),
    path('signup', views.handelSignup, name='signup'),
    path('trainers', views.trainers, name='trainers'),
    path('events', views.events, name='events'),
    # path('pricing', views.pricing, name='pricing'),
    path('course_details', views.course_details, name='course_details'),

    path('edit', views.edit, name='edit'),
    path('my_enrolled_courses', views.my_enrolled_courses, name='my_enrolled_courses'),
    path('handelLogout', views.handelLogout, name='handelLogout'),
    path('homepage_2', views.homepage_2, name='homepage_2'),

]





