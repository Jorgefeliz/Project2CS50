from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_listing(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    #item_id = models.IntegerField()
    item_created = models.DateTimeField()
    item_startbid = models.DecimalField(decimal_places=2, max_digits=7)
    item_title = models.CharField(max_length=255)
    item_description = models.CharField(max_length=510)
    item_url = models.CharField(max_length=512)
    item_category = models.CharField(max_length=64)
    item_active = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f" ({self.pk} {self.user_id} {self.item_title} {self.item_startbid} {self.item_category} {self.item_description} {self.item_url} {self.item_created} {self.item_active})"

#Store the relation between creator and Item
class User_listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_items")
    item_id = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="items_listed")

    def __str__(self):
        return f"{self.user_id} ({self.item_id})"


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Auction_listing, on_delete=models.CASCADE) 
    comment = models.CharField(max_length=510)

    def __str__(self):
        return f"{self.user_id} ({self.item_id}) ({self.comment})"

#Store the relation between watched item and user
class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ManyToManyField(Auction_listing, related_name="item_watched")
    watched = watched = models.BooleanField() 

    def __str__(self):
        return f"{self.watched} ({self.user_id}) ({self.item_id})"





    

    