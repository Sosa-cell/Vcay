from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import BeachHouse, Booking
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('house_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'booking/register.html', {'form': form})

def house_list(request):
	houses = BeachHouse.objects.all()
	return render(request, 'booking/house_list.html', {'houses': houses})

def house_detail(request, house_id):
	house = get_object_or_404(BeachHouse, id=house_id)
	bookings = house.bookings.order_by('start_date')
	return render(request, 'booking/house_detail.html', {'house': house, 'bookings': bookings})

@login_required
def book_house(request, house_id):
	house = get_object_or_404(BeachHouse, id=house_id)
	if request.method == 'POST':
		start_date = request.POST.get('start_date')
		end_date = request.POST.get('end_date')
		# Convert to date objects
		try:
			start_date = date.fromisoformat(start_date)
			end_date = date.fromisoformat(end_date)
		except Exception:
			return render(request, 'booking/book_house.html', {'house': house, 'error': 'Invalid date format.'})
		# Check for conflicts
		conflict = Booking.objects.filter(
			house=house,
			start_date__lt=end_date,
			end_date__gt=start_date
		).exists()
		if conflict:
			return render(request, 'booking/book_house.html', {'house': house, 'error': 'This house is already booked for those dates.'})
		Booking.objects.create(house=house, user=request.user, start_date=start_date, end_date=end_date)
		return redirect(f'/house/{house.id}/?confetti=1')
	return render(request, 'booking/book_house.html', {'house': house})
