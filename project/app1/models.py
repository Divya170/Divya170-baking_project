from django.db import models

# Create your models here.

class table(models.Model):
    name=models.CharField(max_length=30)
    mn=models.IntegerField()
    address=models.CharField(max_length=50)
    email=models.EmailField()
    feedback = models.CharField(max_length=255, default="Default Feedback")




# Product model for the product gallery
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

# About Content model for the About section
class AboutContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# Order model for the order form
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
      return f"Order from {self.name} for {self.product.name}"

