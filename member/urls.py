"""LOGIN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
#from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from django.conf.urls import url
# from .import index

from .api import UserList, UserDetail, UserAuthentication
#from member import views
#from rest_framework import routers

#router = routers.DefaultRouter(trailing_slash=False) 
#router.register('Userdetails', views.Users)


urlpatterns = [

    path('',views.Indexpage),
    path('Home',views.homepage, name="Home"),
    path('Registration', views.UserReg, name="Reg"),
    path('Loginpage', views.loginpage, name="Loginpage"),
    path('Logout',views.logout, name="Logout"),
    path('View',views.view,name="View"),

    path('templates\MainSharing.html',views.mainSharing, name="MainSharing"),
    path('templates\sharing.html',views.sharing, name="Sharing"),
    #path('ViewSharing',views.viewSharing,name="ViewSharing"),
    #path('templates\UpdateSharing',views.updateSharing, name="UpdateSharing"),
    path('templates\DeleteSharing.html', views.deleteSharing, name="DeleteSharing"),

    path('templates\MainGroup.html',views.mainGroup, name="MainGroup"),
    path('templates\group.html',views.group, name="Group"),
    path('templates\MyGroup.html',views.myGroup, name="MyGroup"),

    path('templates\MainMember.html', views.mainMember, name="MainMember"),
    path('templates\member.html',views.member, name="member"),
    path('templates\friendlist.html',views.friendlist, name="friendlist"),
    #path('templates\MyMember.html',views.myMember, name="MyMember"),
    path('templates\MainSearchbar/', views.MainSearchbar, name='MainSearchbar'),

    path('templates\workshop.html',views.workshop, name="Workshop"),
    #path('templates\Booking',views.booking, name="Booking"),
    path('templates\CreateWorkshop.html',views.createWorkshop, name="CreateWorkshop"),

    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<Person>\d+)/$', UserDetail.as_view(), name='user_list'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







