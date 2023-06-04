from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ["birth_date", "phone_number"]
    birth_date = models.DateField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)


class ArtType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Exhibit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    art_type = models.ForeignKey(ArtType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
