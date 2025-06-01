# alx_travel_app

A simple Django application for managing property listings, bookings, and reviews. This project includes models, serializers, and a data seeder for populating the database with sample listings.

---

## Project Structure
```
listings/
├── models.py
├── serializers.py
├── management/
│   └── commands/
│       └── seed.py
```
---
## Features

- Manage **Listings** with title, description, location, and price  
- Book **Listings** with check-in and check-out dates  
- Add **Reviews** for listings with a rating and comment  
- API-ready with Django REST Framework serializers  
- Built-in database seeder for quick testing  

---

## Installation

### Clone the repo

```bash
git clone https://github.com/yourusername/listings-app.git
cd listings-app
```

## Install dependencies
```pip install -r requirements.txt```

## Apply migrations

````python manage.py migrate````

## Create a superuser (optional)
```python manage.py createsuperuser```

## Run the development server
```python manage.py runserver```

## Seeding Sample Data
### Run the custom management command to populate the database with 20 fake listings:
```python manage.py seed```


### `created_at:` DateTimeField

## Serializers
### `ListingSerializer` — Serializes all Listing fields

### `BookingSerializer` — Serializes all Booking fields

## Contributing
Contributions are welcome! Please fork the repo and submit a pull request.

## License
This project is licensed under the MIT License.



