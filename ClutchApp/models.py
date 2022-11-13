from django.db import models
from django.contrib.postgres.fields import ArrayField

# class UserManager(models.Manager):

#     def logValidator(self, postData):
#             errors = {}
#             if postData['password'] != "setPassWord" and postData['password'] != "adminPassword":
#                 errors['password'] = "Password is invalid!"
#             return errors

class User(models.Model):
    password = models.CharField(max_length=80, default="setPassword")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()



class Items(models.Model):
    title = models.CharField(max_length= 80)
    description = models.CharField(max_length= 255)
    price = models.IntegerField(default=None)
    imgNums = ArrayField(models.IntegerField(default=None), size=None, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return str(self.id)

#     @property
#     def get_item_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
    
#     @property
#     def get_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.quantity for item in orderitems])
#         return total

# class OrderItem(models.Model):
#     item = models.ForeignKey(Items, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     @property
#     def get_total(self):
#         total = self.item.price * self.quantity
#         return total

# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     zipcode = models.CharField(max_length=200)
#     country = models.CharField(max_length=200, default="US")
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address

# class Image(models.Model):
#     image = models.ImageField(upload_to='Image/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class GalleryImageDesc(models.Model):
#     description = models.CharField(max_length=255)
#     image = models.IntegerField(default=None)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class GalleryImage(models.Model):
#     image = models.ImageField(upload_to='Gallery', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class EmailList(models.Model):
#     email = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
