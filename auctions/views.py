from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import User, Auction_listing, User_listing, Comment, Watchlist


def index(request):
    #user_item_list = User_listing.objects.filter(user_id = request.user.id)
    item_listing = []
    #for item in user_item_list:
    #    list = Auction_listing.objects.get(pk = item.item_id)
    #    print(list)
    #    item_listing.append(list)
    lists = Auction_listing.objects.filter(item_active = True)
    for lista in lists:
        item_listing.append(lista)
  
    message = "Active listing"
    return render(request, "auctions/index.html",
        {
        "item_listing": item_listing,
        "message": message        
        })


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
        user=User.objects.get(pk=request.user.id) #se obtiene el objeto user
        item_created= datetime.now()

        listing = Auction_listing.objects.create(
            #user = user,
            item_title = item_title,
            item_description = item_description,
            item_url = item_url,
            item_startbid = item_startbid,
            item_category = item_category,
            item_created = item_created,
            item_active = True,
            user_id = user # nuevo

            ) 

        listing.save()

        user_list = User_listing.objects.create(
            
            user_id = user,
            item_id = listing,
            #watched = False
        )
        #print(user.id, " + ", listing.id)        
        
        #user = User.objects.create_user(username, email, password)
        #user.save()
        return render(request, "auctions/create.html", {"categories" : list_categories()})


    else:
        return render(request, "auctions/create.html", {"categories" : list_categories()})

    #Obtener el user , El id del item al ingresarlo en la tabla

def list_categories():
    categories = ['electronics', 'home', 'books', 'smartphones & tablets', 'computer', 'home repair']
    return categories


def auctions(request, item_id):
    item_id = int(item_id)
    lista =Auction_listing.objects.get(pk = item_id) # object
  

    #si no hay usuario logueado
    owner = False
    if request.user.id != None:
        user_id = User.objects.get(pk=request.user.id)
        user_listings = User_listing.objects.filter(user_id = user_id) #queryset
 
        for listing in user_listings:
            if listing.item_id == lista:
                owner = True
                break

    comments = Comment.objects.filter(item_id = lista) 
    comentario = []
    for comment in comments:
        comentario.append(comment)


    return render(request, "auctions/item_bidding.html",{
            "item": lista,
            "comments": comentario,
            "owner": owner,
            "watched": IsWatched(item_id, request.user.id)
            } )

def IsWatched(item_pk, user_pk):
        
    try:
        mirados = Watchlist.objects.filter(item_pk = item_pk).get(user_pk = user_pk)
        return True

    except Watchlist.DoesNotExist:
        return False   
      

def bidding (request):
    if request.method == "POST":
        new_bid = float(request.POST.get("new_bid"))
        item_pk = request.POST.get("item_pk")
                    
        try:
            lista = Auction_listing.objects.get(pk = item_pk)

        except:
            print("AQUI 2 ")
            print(new_bid)
            print(item_pk)
            # que hacer cuando hay un error

        if lista.item_active == True:
            if lista.item_startbid <= new_bid:
                lista.item_startbid = new_bid
                #checking is the user is bidding on his own item
                user = User.objects.get(pk=request.user.id)
                if lista.user_id == user:
                    message = "You cannot bid on your own item"
                    return render(request, "auctions/error.html", {"message" : message })
            
                lista.user_id = user #nuevo 
                lista.save()
                # render page with the new value
            
            else:
                message = "Please enter a higher bid"
                return render(request, "auctions/error.html", {"message" : message })
        
        else:
            message = "The auction is already closed"
            return render(request, "auctions/error.html", {"message" : message })

     
        return HttpResponseRedirect(reverse("auctions", kwargs={"item_id": item_pk}))

@login_required()
def closing(request):
    item_pk = request.POST.get("item_pk")
    lista = Auction_listing.objects.get(pk = item_pk)
    lista.item_active = False
    lista.save()

    return HttpResponseRedirect(reverse("auctions", kwargs={"item_id": item_pk}))

@login_required()
def won_listing(request):
    user = User.objects.get(pk=request.user.id)
    lista = Auction_listing.objects.filter(user_id = user).filter(item_active=False)
    won = []
    for item in lista:
        won.append(item)
    
    message = "Items Won"
    return render(request, "auctions/index.html", {
        "item_listing" : won,
        "message": message
         })

@login_required()
def comment(request):
    comment = request.POST["comment"]
    item_pk= request.POST["item_pk"]

    user = User.objects.get(pk=request.user.id)
    lista = Auction_listing.objects.get(pk = item_pk)
    post = Comment.objects.create(
        user_id = user,
        item_id = lista,
        comment = comment
    )

    post.save()

    return HttpResponseRedirect(reverse("auctions", kwargs={"item_id": item_pk}))

def watchlist(request):
    user_pk = request.user.id

    mirados = Watchlist.objects.filter(user_pk = user_pk)
 
    watched_id = []
    for vista in mirados:
        watched_id.append(vista)    
    
    watched = []
    for item in watched_id:
        watched.append(Auction_listing.objects.get(pk = item.item_pk))

    

    message = "Watchlist"
    return render(request, "auctions/index.html", {
        "item_listing" : watched,
        "message": message
         })

def watch(request, item_id):
    item_pk = int(item_id)
    user_pk = request.user.id
    
    try:
        mirados = Watchlist.objects.filter(item_pk = item_pk).get(user_pk = user_pk)
        print(mirados)
    except Watchlist.DoesNotExist:
        watched = Watchlist.objects.create(
            user_pk = user_pk,
            item_pk = item_pk,
        )
        watched.save()
        return HttpResponseRedirect(reverse("auctions", kwargs={"item_id": item_pk}))
    
    mirados.delete()

    return HttpResponseRedirect(reverse("auctions", kwargs={"item_id": item_pk}))

def categories(request):
    if request.method == "POST":
        item_category = request.POST["category"]
        lista = Auction_listing.objects.filter(item_category = item_category)
        item_listing = []

        for item in lista:
            item_listing.append(item)
        
        message = "Category Search"
        return render(request, "auctions/index.html",
        {
        "item_listing": item_listing,
        "message": message        
        })

    else:
        message = "Search by Categories"
        return render(request, "auctions/category.html",
        {"message" : message,
        "categories" : list_categories()
        })