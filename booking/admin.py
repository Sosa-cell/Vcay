from django.contrib import admin
from .models import BeachHouse, Booking

@admin.register(BeachHouse)
class BeachHouseAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('house', 'user', 'start_date', 'end_date', 'created_at')
	list_filter = ('house', 'start_date', 'end_date', 'user')
	search_fields = ('house__name', 'user__username')
