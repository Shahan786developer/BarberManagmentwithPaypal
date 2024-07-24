import datetime
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate,logout #add this
from datetime import datetime, timedelta


def index(request):
    rev = Review.objects.all()
    
    return render(request, 'barapp/index.html',{'rew':rev})

def profile(request):
    orders = Order.objects.filter(user=request.user)  
    return render(request, 'barapp/profile.html', {'orders': orders,})



def log_in(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("index")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()
  return render(request=request, template_name="barapp/login.html", context={"login_form":form})


def reg(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        else:
            # Check for specific error codes and create separate messages
            if 'username' in form.errors:
                messages.error(request, "Username already exists.")
            if 'password2' in form.errors:
                messages.error(request, "Passwords do not match.")
            # Add more conditions for other error types as needed
            # ...

    else:
        form = NewUserForm()

    return render(request=request, template_name='barapp/reg.html', context={"register_form": form})
def log_out(request):
    logout(request)
    return redirect('login')


def order_list(request):
    # Retrieve all services
    

    # Filter orders for the current user and those that are not completed
    orders = Order.objects.filter(user=request.user, completed=False)
    
    # Pass both orders and services to the template context
    return render(request, 'barapp/orderview.html', {'orders': orders,})

def completed_order_list(request):
    ser =Service.objects.all()
    completed_orders = Order.objects.filter(user=request.user, completed=True)
    return render(request, 'barapp/orderscompleted.html', {'completed_orders': completed_orders})
def order(request):
    ser =Service.objects.all()
    if request.method == "POST":
        o_form = OrderForm(request.POST, request.FILES)
        o_form.instance.user = request.user
        if o_form.is_valid():
            o_form.save()
            messages.success(request, 'Your order was successfully added!')
            return redirect('orders')  # Redirect to the orders page after successful submission
        else:
            # Provide more specific error message to the user
            messages.error(request, 'Error saving form. Please check your inputs.')

    else:  # If it's a GET request or the form is not valid
        o_form = OrderForm()

    return render(request=request, template_name="barapp/order.html", context={'orderform': o_form,'services':ser})

def update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    services = Service.objects.all()

    # Pre-select services that are already associated with the order
    selected_services = order.services.all()
    for service in services:
        if service in selected_services:
            service.checked = True
        else:
            service.checked = False

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'order': order, 'orderform': form, 'services': services}
    return render(request, 'barapp/update.html', context)

def delete(request, pk):

  order = Order.objects.get(id=pk)
  if request.method == 'POST':
   order.delete()

   return redirect('order')

  context = {'order': order}

  return render(request, 'barapp/delete.html',context)
def deleteall(request):
  delall = Order.objects.filter(user=request.user)
  delall.delete()
    
  return redirect('order')


def review(request):
    ser =Worker.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('allrev')  # Redirect to a success page
    else:
        form = ReviewForm()
    return render(request, 'barapp/review.html', {'form': form,'worker':ser})

def review_success(request):
    return render(request, 'yourapp/review_success.html')
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'barapp/reviewlist.html', {'reviews': reviews})
def toggle_like(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    user = request.user

    if user in review.likes.all():
        review.likes.remove(user)
    else:
        review.likes.add(user)

    # Redirect back to the same page after processing the like/unlike
    return redirect('allrev')


def weekly_report(request):
    
    orders = Order.objects.filter(user=request.user)
    return render(request, 'barapp/weeklyreport.html',  {'orders': orders})

def AboutBarber(request):
    reviews = ShopReview.objects.all()

    return render(request, 'barapp/aboutbarber.html',{'review':reviews})
def AddTOBarberSHop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('AboutBarber')  # Change 'review_list' to the name of your review listing URL
    else:
        form = ReviewForm()
    return render(request, 'barapp/addtobarbershop.html', {'form': form})