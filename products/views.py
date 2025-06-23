from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess, os

def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'products/home.html', {'products': products})

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

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        order = Order.objects.create(name=name, phone=phone, address=address)
        order.products.set(products)
        request.session['cart'] = []

        return render(request, 'products/order_summary.html', {
            'products': products,
            'name': name,
            'phone': phone,
            'address': address
        })

    return render(request, 'products/place_order.html', {'products': products})

@csrf_exempt
def deploy(request):
    if request.method == "POST":
        try:
            output = subprocess.check_output(
                ["git", "pull"],
                cwd="/home/vineeey/vinaymobiles"
            )
            os.system("touch /var/www/vineeey_pythonanywhere_com_wsgi.py")
            return HttpResponse(f"Deployment complete:\n{output.decode()}")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Deployment failed:\n{e}", status=500)
    return HttpResponse("Only POST method allowed", status=405)
