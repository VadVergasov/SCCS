from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


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
    date_arrived = models.DateField(auto_now_add=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def delete(self, using=None, keep_parents=False):
        responsible_user = User.objects.filter(groups__name="Сотрудники").first()

        if responsible_user:
            self.responsible = responsible_user
            self.save()

        super().delete(using=using, keep_parents=keep_parents)

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    floor = models.IntegerField(null=True)
    area = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Tour(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
    cost = models.IntegerField()
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    creation_time = models.TimeField(auto_now=True)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    content = models.TextField()
    mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    creation_time = models.TimeField(auto_now=True)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
