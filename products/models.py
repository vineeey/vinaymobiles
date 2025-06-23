from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, default='Apple')
    model_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.CharField(max_length=20)  # e.g. 128GB, 256GB
    color = models.CharField(max_length=30)
    display_size = models.CharField(max_length=20)
    camera = models.CharField(max_length=50)
    battery = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.storage} - {self.color}"

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.name} – {self.created_at.strftime('%b %d, %Y')}"
