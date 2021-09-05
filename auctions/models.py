from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    #items_watched = models.ManyToManyField(Auction_listing, blank=True , through="Watchlist" , related_name="items_watched")

    pass

class Auction_listing(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    #item_id = models.IntegerField()
    item_created = models.DateTimeField()
    item_startbid = models.FloatField()
    item_title = models.CharField(max_length=255)
    item_description = models.CharField(max_length=510)
    item_url = models.CharField(max_length=512)
    item_category = models.CharField(max_length=64)
    item_active = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #users_watching = models.ManyToManyField(User, blank=True , through="Watchlist" , related_name="users_watching")

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
    user_pk = models.IntegerField()
    item_pk = models.IntegerField()

    def __str__(self):
        return f"{self.user_pk} ({self.item_pk})"








    

    