from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Product(models.Model):
    productname=models.CharField(max_length=200)
    capacity=models.CharField(max_length=200)
    price=models.BigIntegerField()
    description=models.TextField()
    image=models.ImageField()
    
    class Meta:
        db_table = 'product'

class Suppliers(models.Model):
    branchname = models.CharField(max_length=200)
    ownername = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    stock = models.IntegerField()
    approval = models.IntegerField()
    
    class Meta:
        db_table = 'suppliers'
        
        
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='areas', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class User_profile(models.Model):
    phone = models.BigIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'user_profile'
        

class Feedback(models.Model):
    rating = models.IntegerField()
    Message = models.TextField()
    user = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'feedback'
        
class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=200)
    Message = models.TextField()
   
    class Meta:
        db_table = 'inquiry' 
        


    
    
class Product_Category(models.Model):
    category_name =models.CharField(max_length=30)
    image=models.ImageField()
    
    class  Meta:
        db_table = 'product_category'


        
    


class SoftDrink(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='softdrinks/')
    size = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Product_Category, related_name='categoryid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'softdrink'


class Order(models.Model):
    quantity = models.IntegerField()
    order_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_deliver = models.DateTimeField()
    payments = models.CharField(max_length=50)
    payment_id = models.TextField()
    user = models.ForeignKey(User, related_name='userid', on_delete=models.CASCADE)
    softdrink = models.ForeignKey(SoftDrink, related_name='softdrinkid', on_delete=models.CASCADE)  # Corrected name to lowercase 'softdrink'
    supplier = models.ForeignKey('Suppliers', related_name='supplierid', on_delete=models.CASCADE)
    approval = models.IntegerField()
    track = models.IntegerField()

    class Meta:
        db_table = 'order'