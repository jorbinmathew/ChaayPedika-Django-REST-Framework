from django.db import models

# Create your models here.
class categorydb(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class productdb(models.Model):
    category=models.ForeignKey(categorydb,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.DecimalField()
    def __str__(self):
        return self.product_name