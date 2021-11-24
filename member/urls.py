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
from django.contrib import admin, auth
from django.urls import path
from django.conf.urls import url, include
#from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import authentication
from rest_framework_simplejwt.views import TokenRefreshView

#from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
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
    path('HomeAdmin',views.homepageAdmin, name="HomeAdmin"),
    path('Registration', views.UserReg, name="Reg"),
    path('Loginpage', views.loginpage, name="Loginpage"),
    path('Logout',views.logout, name="Logout"),
    path('View',views.view,name="View"),

    path('MainSharing.html',views.mainSharing, name="MainSharing"),
    path('sharing.html',views.sharing, name="Sharing"),
    path('ViewSharing',views.viewSharing,name="ViewSharing"),
    path('UpdateSharing',views.updateSharing, name="UpdateSharing"),
    path('DeleteSharing.html', views.deleteSharing, name="DeleteSharing"),

    path('MainGroup.html',views.mainGroup, name="MainGroup"),
    path('group.html',views.group, name="Group"),
    path('MyGroup.html',views.myGroup, name="MyGroup"),
    path('CreategroupAdmin.html',views.GroupAdmin, name="GroupAdmin"),
    path('EditGroup.html',views.updateGroup, name="EditGroup"),

    path('MainMember.html', views.mainMember, name="MainMember"),
    path('member.html',views.member, name="member"),
    path('friendlist.html',views.friendlist, name="friendlist"),
    #path('MyMember.html',views.myMember, name="MyMember"),
    path('MainSearchbar', views.MainSearchbar, name='MainSearchbar'),

    path('workshop.html',views.workshop, name="Workshop"),
    path('booking.html',views.booking, name="Booking"),
    path('CreateWorkshop.html',views.createWorkshop, name="CreateWorkshop"),
    path('BookWorkshop.html',views.BookWorkshop, name="BookWorkshop"),

    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    #url(r'^api/users_list/(?P<Person>\d+)/$', UserDetail.as_view(), name='user_list'),
    #url(r'^api/auth/$', UserAuthentication.as_view(), name='auth'),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







