from django.urls import path
from .views import create_booking,login_user,booking_status,register_user,admin_dashboard,update_booking_status,list_orders

urlpatterns = [
    path('', login_user, name = 'login_user'),
    path('register',register_user, name= 'register_user'),
    path('booking', create_booking, name='create_booking'),
    path('booking-status/<int:booking_id>/',booking_status,name='booking_status'),
    path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
    path('update-booking/<int:booking_id>/',update_booking_status, name='update_booking_status'),
    path('list-orders/',list_orders, name='list_orders'),
]