from rest_framework import serializers
from .models import Listing, Booking, Review, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_host', 'phone_number', 'profile_image'
        ]


class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'location',
            'price_per_night', 'max_guests', 'host',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'host', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'user', 'check_in_date', 'check_out_date',
            'guests', 'total_price', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'total_price', 'status', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'listing', 'user', 'rating', 'comment',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
