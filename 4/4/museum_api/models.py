from django.db import models


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


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.ForeignKey("Position", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
