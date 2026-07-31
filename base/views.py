from django.shortcuts import render, redirect,get_object_or_404
from .models import Flight, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from datetime import date

@login_required
def home(request):
    flights = Flight.objects.all()
    from_city = request.GET.get('from_city')
    to_city = request.GET.get('to_city')

    if from_city and to_city:

        flights = Flight.objects.filter(
            from_city__icontains=from_city,
            to_city__icontains=to_city
        )
    return render(request,'home.html',{'flights': flights})


@login_required
def booknow(request, id):

    flight = Flight.objects.get(id=id)

    if request.method == 'POST':

        Booking.objects.create(
            flight=flight,
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            aadhaar=request.POST['aadhaar'],
            age=request.POST['age'],
            seat_class=request.POST['seat_class'],
            seat_number=request.POST['seat_number']
        )

        return redirect('history')

    return render(request,'booknow.html',{'flight': flight})


@login_required
def history(request):

    bookings = Booking.objects.filter(
        flight__date__lt=date.today()
    )

    return render(request,'history.html',{'bookings': bookings})


@login_required
def cancel_booking(request, id):

    booking = get_object_or_404(Booking, id=id)

    booking.delete()

    return redirect('history')


@login_required
def update_booking(request, id):

    booking = Booking.objects.get(id=id)

    if request.method == 'POST':

        booking.name = request.POST['name']
        booking.email = request.POST['email']
        booking.phone = request.POST['phone']
        booking.aadhaar = request.POST['aadhaar']
        booking.age = request.POST['age']
        booking.seat_class = request.POST['seat_class']
        booking.seat_number = request.POST['seat_number']

        booking.save()

        return redirect('history')

    return render(request,'update_booking.html',{'booking': booking})



@login_required
def profile(request):

    return render(request,'profile.html')

@login_required
def update_profile(request):

    if request.method == 'POST':

        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']

        request.user.save()

        return redirect('profile')

    return render(request,'update_profile.html')

@login_required
def change_password(request):

    if request.method == 'POST':

        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect')
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('change_password')

        request.user.set_password(new_password)
        request.user.save()

        update_session_auth_hash(request, request.user)

        messages.success(request, 'Password changed successfully')
        return redirect('profile')

    return render(request, 'change_password.html')


def about(request):
    return render(request,'about.html')


def support(request):
    return render(request,'support.html')



def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        messages.success(request, 'Registration Successful')
        return redirect('user_login')

    return render(request, 'register.html')



def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('home')

        else:

            messages.error(
                request,
                'Invalid Username or Password'
            )

    return render(request,'user_login.html')


def user_logout(request):

    logout(request)

    return redirect('user_login')


def bookings(request):

    bookings = Booking.objects.filter(
        flight__date__gte=date.today()
    )

    return render(request,'bookings.html',{'bookings': bookings})

# Create your views here.
