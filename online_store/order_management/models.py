from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=7)

class Articles(models.Model):
    name=models.CharField(max_length=30)
    section=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return 'The name is %s the section is %s the price is %s' %(self.name, self.section, self.price)

class Orders(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    delivered=models.BooleanField()
