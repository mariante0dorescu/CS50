from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import *

def checkOwner(req, lis):
    if req.user.id == lis.user.id:
        return True


def index(request):
    listings = Listing.objects.all().filter(active=True)
    
    return render(request, "auctions/index.html", {
        "listings" : listings,
    })


def categories(request):
    categories = Category.objects.all()
    
    return render(request, "auctions/category_list.html", {
        "categories" : categories,
        
    })


def category(request, str):
    category = get_object_or_404(Category, name=str)
    listings = Listing.objects.all().filter(category=category)
    
    return render(request, "auctions/index.html", {
        "listings" : listings,
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


def listing(request, pk):

    listing = get_object_or_404(Listing, pk=pk)
    last_bid = Bid.objects.filter(listing=listing).last()
    comments = Comment.objects.filter(listing=listing)
    watching = Watching.objects.filter(user=request.user.id, listing=listing.id).exists()  

    context = { 
        "listing" : listing,
        'bid': last_bid,
        "comments":comments,
        "owner": checkOwner(request,listing),
        "watching": watching,
        }

    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        elif "bid_amount" in request.POST:
            form_bid = float(request.POST['bid_amount'])

            if form_bid > last_bid.bid:
                new_bid = Bid(user=request.user, listing=listing, bid=form_bid)
                new_bid.save()
                return HttpResponseRedirect(reverse('listing', args=[pk]))
            else:
                bid_error = "Bid must be greater than last bid"
                context["bid_error"] = bid_error
                context["bid"] = form_bid
                return render(request, "auctions/listing.html", context)

        elif "close" in request.POST:
            if checkOwner(request, listing):
                listing.winner = User.objects.get(id=last_bid.user.id)
                listing.save()
                print(listing.active)
                return HttpResponseRedirect(reverse('listing', args=[pk]))

        elif "comment" in request.POST:
            new_comment = request.POST['comment']
            if new_comment.strip():
                new_comment = Comment(user=request.user, listing=listing, comment=new_comment)
                new_comment.save()
                return HttpResponseRedirect(reverse('listing', args=[pk]))
            else:
                comment_error = "Please enter a comment"
                context["comment_error"] = comment_error
                return render(request, "auctions/listing.html", context)


    return render(request, "auctions/listing.html", context)


@login_required(login_url='/login/')
def watching_list(request):
    items = Watching.objects.all().filter(user=request.user).values_list('listing', flat=True)
    listings = Listing.objects.filter(pk__in=items)

    return render(request, "auctions/watched_items.html", {
        "listings" : listings,
    })


@login_required(login_url='/login/')
def watch(request, pk):
    item = get_object_or_404(Listing, pk=pk)
    item_exists = Watching.objects.filter(user=request.user.id, listing=item.id).exists()

    if item_exists:
        return HttpResponse('Item is already on your watch.')
    else:
        user_list, created = Watching.objects.get_or_create(user=request.user)
        user_list.listing.add(item)
        return HttpResponseRedirect(reverse('listing', args=[pk]))


@login_required(login_url='/login/')
def unwatch(request, pk):
    item = get_object_or_404(Listing, pk=pk)    
    user_list = Watching.objects.get(user=request.user)
    try:
        user_list.listing.remove(item)
        previous_page = request.META.get('HTTP_REFERER')
        if previous_page:
            print(previous_page)
            return redirect(previous_page)
        else:
            return HttpResponseRedirect(reverse('listing', args=[pk]))

    except Watching.DoesNotExist:
        return HttpResponse('Item is not on your watch.')


def categories_all(request):
    categories = Category.objects.all()
    categories_listings = {}
    for category in categories:
        listings = Listing.objects.filter(category=category)
        categories_listings[category] = listings
   
    return render(request, 'auctions/all_categories.html', {
        'categories_listings': categories_listings
    })

def create(request):

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        title = request.POST['title'].strip()
        description = request.POST['description'].strip()
        image = request.FILES.get('image')
        starting = int(request.POST['starting'])
        category = Category.objects.get(name=request.POST['category'])
        print(starting)

        new_listing = Listing(user=user, title=title, description=description, image=image, starting=starting, category=category)
        new_listing.save()
        return HttpResponseRedirect(reverse('index'))

    context ={
      "categories": Category.objects.all()
    } 
    return render(request, 'auctions/create.html', context)