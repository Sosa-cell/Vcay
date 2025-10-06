
from django.db import models
from django.contrib.auth.models import User

class BeachHouse(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	house = models.ForeignKey(BeachHouse, on_delete=models.CASCADE, related_name='bookings')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('house', 'start_date', 'end_date')
		ordering = ['start_date']

	def __str__(self):
		return f"{self.house.name} booked by {self.user.username} from {self.start_date} to {self.end_date}"

	def conflicts(self):
		# Check for conflicting bookings
		return Booking.objects.filter(
			house=self.house,
			start_date__lt=self.end_date,
			end_date__gt=self.start_date
		).exclude(id=self.id).exists()
