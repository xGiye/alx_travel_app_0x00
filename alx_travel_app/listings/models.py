from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_host = models.BooleanField(default=False)  # Indicates if the user can create listings
    phone_number = models.CharField(max_length=20, blank=True)
    profile_image = models.URLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Keep username for compatibility

    def __str__(self):
        return self.email


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.FloatField()
    max_guests = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests = models.PositiveIntegerField()
    total_price = models.FloatField()
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user.email} for {self.listing.title}"


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # Typically 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('listing', 'user')  # Prevent multiple reviews per listing per user

    def __str__(self):
        return f"Review by {self.user.email} - {self.rating}★"
