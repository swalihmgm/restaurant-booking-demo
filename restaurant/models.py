
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )
    ITEM_CHOICES = [
        ('biriyani', 'Chicken Biriyani'),
        ('beef_biriyani', 'Beef Biriyani'),
        ('mutton_biriyani', 'Mutton Biriyani'),
        ('fried_rice', 'Fried Rice'),
        ('noodles', 'Noodles'),
        ('mandhi', 'Chicken Mandhi'),
        ('alfaham', 'Alfaham'),
        ('shawarma', 'Shawarma'),
        ('burger', 'Burger'),
        ('pizza', 'Pizza'),
        ('porotta', 'Porotta'),
        ('chicken_curry', 'Chicken Curry'),
        ('beef_curry', 'Beef Curry'),
        ('fish_fry', 'Fish Fry'),
        ('ice_cream', 'Ice Cream'),
        ('juice', 'Fresh Juice'),
        ('tea', 'Tea'),
        ('coffee', 'Coffee'),
]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    customer_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    item = models.CharField(max_length=50, choices=ITEM_CHOICES)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)


