from django.db import models
# from _auth.models import CustomUser
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg',
                            upload_to='product_images')

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_item_price(self):
        return self.item.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_item_price()
        return total