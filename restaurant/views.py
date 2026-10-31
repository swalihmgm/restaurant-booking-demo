from django.shortcuts import render,redirect, get_object_or_404
from .forms import Booking_form, Register_form, Login_form, BookingStatus_Form
from .models import Booking
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_user')
def create_booking(request):
    if request.method == "POST":
        form = Booking_form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_status', booking_id = booking.id)
    else:
        form = Booking_form()

    return render(request, 'restaurant/create_booking.html', {
        'form': form,
        'username':request.user.username
    })

def booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'restaurant/booking_status.html',{'booking':booking})

def register_user(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            costomer_group = Group.objects.get(name='customer')
            user.groups.add(costomer_group)
            login(request,user)
            return redirect('create_booking')
    form = Register_form()
    return render(request, 'restaurant/register.html',{'form':form} )

def login_user(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                login(request,user)
                if user.groups.filter(name='admin').exists():
                    return redirect('admin_dashboard')
                return redirect('create_booking')
    else:
        form = Login_form()
    return render(request, 'restaurant/login.html', {'form':form})

def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, 'restaurant/admin_dashboard.html',{'bookings':bookings})

def update_booking_status(request,booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingStatus_Form(request.POST, instance= booking)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    return redirect('admin_dashboard')

@login_required(login_url='login_user')
def list_orders(request):
    orders = Booking.objects.filter(user = request.user)
    return render(request, 'restaurant/orders.html',{'orders':orders})