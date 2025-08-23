from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Address(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    street=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.street},{self.city}'

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100) 
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,related_name='orders')
    order_date=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digits=10,decimal_places=3,default=0.00)
    
    def calculate_total_price(self):
        self.total_price=sum(product.price for product in self.products.all())
        self.save()
    def __str__(self):
        return f'order {self.id} by {self.customer.name}'
    