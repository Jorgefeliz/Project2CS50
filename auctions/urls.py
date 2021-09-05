from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auctions/<str:item_id>", views.auctions, name="auctions"),
    path("bidding", views.bidding, name="bidding"),
    path("closing", views.closing, name="closing"),
    path("won_listing", views.won_listing, name="won_listing"),
    path("comment", views.comment, name="comment"),
    path("watch/<str:item_id>", views.watch, name="watch"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories")
]
