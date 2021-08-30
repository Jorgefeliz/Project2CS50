from django.contrib import admin

from .models import Auction_listing,Bids,Comment, User, User_listing
# Register your models here.

admin.site.register(Auction_listing)
admin.site.register(Bids)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(User_listing)