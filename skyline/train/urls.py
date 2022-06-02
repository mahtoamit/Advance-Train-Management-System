
from .models import Add_Train
from django.contrib import admin
from django.urls import path
from train.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name="home"),
    path('admindash',admindash,name="admindash"),
    path('adminindex',adminindex,name="adminindex"),
    
    path('registercustomer',Register_customer,name="registercustomer"),
    path('viewregusers', view_regusers, name="viewregusers"),
    path('login',Login_customer,name="login"),
    path('delete_user/<int:pid>',delete_user, name="delete_user"),
    path('log_out',Logout,name="log_out"),

    
    path('addtrain', Add_Trai, name="addtrain"),
    path('viewtrain', viewtrai, name="viewtrain"),
    path('edittrain/?P<pid>[0-9]+)', edit, name="edittrain"),
    path('delete/?P<pid>[0-9]+)', delete, name="delete"),
    
    path('addroute', add_route, name="addroute"),
    path('editroute/?P<pid>[0-9]+)', Edit_route, name="editroute"),
    path('delete_route/?P<pid>[0-9]+)', delete_route, name="delete_route"),
    path('availableroute', displayroute, name="availableroute"),

# USER DASHBOARD STARTS

    path('searchtrain',Search_Train,name="searchtrain"),
    path('bookdetail/(?P<coun>[0-9]+)/(?P<pid>[0-9]+)/(<str:route1>)',Book_detail,name="book_detail"),
    path('delete_passenger/(?P<pid>[0-9]+)/(?P<bid>[0-9]+)/(<str:route1>)',Delete_passenger,name="delete_passenger"),
    path('mybooking',my_booking,name="my_booking"),
    path('delte_my_booking/(?P<pid>[0-9]+)',delte_my_booking,name="delte_my_booking"),
    path('viewbookings', viewbookings, name="viewbookings"),
    path('userdash/',Dashuser,name="userdash"),
    path('card_detail/(?P<total>[0-9]+)/(?P<coun>[0-9]+)/(<str:route1>)/(?P<pid>[0-9]+)',Card_Detail,name="card_detail"),
    path('viewticket/(?P<pid>[0-9]+)',view_ticket, name="viewticket"),

]
