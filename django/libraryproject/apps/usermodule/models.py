from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

class Card(models.Model):
    card_number = models.IntegerField() 

class Student2(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


class Address3(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student3(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ManyToManyField(Address3)


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

