from django.db import models
from django.contrib.auth.models import AbstractUser


class Students(AbstractUser):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField(default=30)
    open_seats = models.IntegerField(default=30)

    def add(self):
        if self.open_seats > 0:
            self.open_seats = self.open_seats - 1
            self.save()

    def drop(self):
        if self.open_seats < self.capacity:
            self.open_seats = self.open_seats + 1
            self.save()
