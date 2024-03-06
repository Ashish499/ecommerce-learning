from django.db import models

class Discount(models.Model):
    name=models.CharField(max_length=88)
    p_percent=models.IntegerField()
    status=models.TextField()
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=88)

    def __str__(self):
        return self.title


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField
    description=models.TextField()
    image=models.ImageField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    qty=models.IntegerField()

    def __str__(self):
        return self.title
    




