# Vcay Beach House Booking App

A Django web application for booking and managing three family beach houses. Designed for private use, it allows family members to view availability, book stays, and avoid scheduling conflicts—all with a modern, fun interface.

## Features
- **Three Beach Houses**: Each with its own calendar and details
- **User Registration & Login**: Only registered users can book
- **Booking System**: Book available dates, see existing bookings, and prevent conflicts
- **Admin Management**: Admins can manage houses and bookings via Django admin
- **Modern UI**: Clean, pastel-themed design inspired by leartify.ca, using the Fredoka font
- **Mobile Friendly**: Responsive layout for all devices

## How It Works
1. **View Houses**: See all available beach houses and their details
2. **Check Availability**: View each house’s calendar and current bookings
3. **Book a Stay**: Log in, select dates, and book if available (no double-booking)
4. **Manage Bookings**: Users can see their bookings; admins can manage all

## Code Usage
- **Python 3.10+** and **Django 5.x**
- Main app: `booking/`
  - Models: `BeachHouse`, `Booking`
  - Views: List, detail, booking, registration
  - Templates: All main pages in `booking/templates/booking/`
  - Static files: CSS in `booking/static/booking/style.css`
- User authentication: Django built-in, with custom registration
- Admin: Register models in `booking/admin.py`

## Setup & Deployment
1. Clone the repo:  
   `git clone https://github.com/Sosa-cell/Vcay.git`
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run migrations:  
   `python manage.py migrate`
4. Create a superuser:  
   `python manage.py createsuperuser`
5. Start the server:  
   `python manage.py runserver`
6. Access at:  
   `http://localhost:8000/`

For free hosting, see the PythonAnywhere setup instructions in this repo or ask for help.

## License
Private/family use only. Not for commercial distribution.

---
Questions or feedback? Open an issue or contact the maintainer.
