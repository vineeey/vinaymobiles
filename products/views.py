from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'products/home.html', {'products': products})
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
        request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    return render(request, 'products/cart.html', {'products': products})

def remove_from_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
        request.session['cart'] = cart
    return redirect('view_cart')

def place_order(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)

    # For now, we're just displaying a thank-you page
    request.session['cart'] = []  # Clear the cart after "order"
    return render(request, 'products/order_summary.html', {'products': products})
# products/views.py

from django.http import HttpResponse
import os
import subprocess


