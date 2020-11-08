from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about',About.as_view(),name="about"),
    path('registations',UserRegistations.as_view(),name = 'registations'),
    path('userlogin',UserLogin.as_view(),name='user_login'),
    path('dashaboard',Dashaboard.as_view(),name="dashaboard"),
    path('applynewservice',ApplyNewService.as_view(),name="applynewsevice"),
    path('pandingrequest',PandingRequest.as_view(),name="pandingrequest"),
    path('apseptrequest',AproveRequest.as_view(),name="aprove"),
    path('reject',RejectRequest.as_view(),name="reject"),
    path('userlogout',UserLogout.as_view(),name="userlogout"),



    #-------------------------------------  Admin Work ------------------------------#

    path('adminlogin',AdminLogin.as_view(),name = 'admin_login'),
    path('dashaboard',AdminDashaboard.as_view(),name = 'admindashaboard'),
    path('allrequestsevice',RequestSevice.as_view(),name="requestservice"),
    path('aproveservice/<int:pk>',AproveService.as_view(),name = 'aproverequest'),
    path('servicing',Servicing.as_view(),name="servicing"),
    path('complitesevice/<int:pk>',Complite.as_view(),name="complite"),
    path('complateservicing',ComplateServicing.as_view(),name="complite"),
    path('adminlogout',AdminLogout.as_view(),name="adminlogout"),

]
