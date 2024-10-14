from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    license_plate = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    EVENT_CHOICES = [
        ('motion_detected', 'Motion Detected'),
        ('car_moved', 'Car Moved Without Key'),
    ]

    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)  # Relación con Driver

    def __str__(self):
        return f"{self.get_event_type_display()} at {self.timestamp}"