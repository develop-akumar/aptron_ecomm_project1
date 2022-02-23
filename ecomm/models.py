import datetime
from django.db import models


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class register_info(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.fname


class product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'upload/product')
    category = models.ForeignKey(category, on_delete=models.CASCADE, default = 1)
    price =models.IntegerField(default = 100)
    description = models.CharField(max_length=255, default='good')


    def __str__(self):
        return self.name


class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(register_info, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.date