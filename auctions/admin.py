from django.contrib import admin

from .models import Auction_listing,Comment, User, User_listing,Watchlist
# Register your models here.

admin.site.register(Auction_listing)
admin.site.register(Watchlist)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(User_listing)