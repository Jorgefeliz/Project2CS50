from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import User, Auction_listing, User_listing


def index(request):
    user_item_list = User_listing.objects.filter(user_id = request.user.id)
    item_listing = []
    for item in user_item_list:
        list = Auction_listing.objects.get(pk = item.item_id)
        print(list)
        item_listing.append(list)
  

    return render(request, "auctions/index.html",
        {"item_listing": item_listing} )


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required()
def create(request):
    if request.method == "POST":
    #Obtener el user , El id del item al ingresarlo en la tabla
        item_title = request.POST["title"]
        item_description = request.POST["description"]
        item_url = request.POST["url"]
        item_startbid = request.POST["startbid"]
        item_category = request.POST["category"]
        user=User.objects.get(pk=request.user.id)
        item_created= datetime.now()

        listing = Auction_listing.objects.create(
            #user = user,
            item_title = item_title,
            item_description = item_description,
            item_url = item_url,
            item_startbid = item_startbid,
            item_category = item_category,
            item_created = item_created,
            item_active = True
            ) 

        listing.save()

        user_list = User_listing.objects.create(
            user_id = user.id,
            item_id = listing.id
        )
        print(user.id, " + ", listing.id)        
        
        #user = User.objects.create_user(username, email, password)
        #user.save()
        categories = ['electronics', 'home', 'books', 'smartphones & tablets', 'computer', 'home repair']
        return render(request, "auctions/create.html", {"categories" : categories})


    else:
       
        print (request.user)
        
        categories = ['electronics', 'home', 'books', 'smartphones & tablets', 'computer', 'home repair']
        return render(request, "auctions/create.html", {"categories" : categories})

    #Obtener el user , El id del item al ingresarlo en la tabla

