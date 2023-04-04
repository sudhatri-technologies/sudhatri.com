
from django.urls import path,include
from sstech import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('web-development',views.webDevelopment,name='web'),
    path('mobile-development',views.mobileDevelopment,name='mobile'),
    path('digital-marketing',views.digitalMarketing,name='dm'),
    path('us-staffing',views.usStaffing,name='us'),
    path('domestic-staffing',views.domesticStaffing,name='ds'),
    path('careers',views.careers,name='careers'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('blog/<slug:slug>/',views.blogDetail,name='blogDetail')
]
