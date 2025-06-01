from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with sample listing data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding listings...")

        # Ensure at least one user exists to be a host
        if not User.objects.exists():
            self.stdout.write("Creating default host user...")
            host_user = User.objects.create_user(username='hostuser', email='host@example.com', password='password123')
        else:
            host_user = User.objects.first()

        # Create sample listings
        for _ in range(20):
            Listing.objects.create(
                host=host_user,
                name=fake.company(),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 300), 2)
            )

        self.stdout.write(self.style.SUCCESS("✅ Seeded 20 sample listings."))
