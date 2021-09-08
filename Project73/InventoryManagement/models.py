from django.db import models

class Product(models.Model):
    Date=models.DateField()
    Provider=models.CharField(max_length=30)
    Name_of_product=models.CharField(max_length=30)
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Amount=models.FloatField()
    Stock=models.IntegerField()


    def __str__(self):
        return self.Name_of_product






