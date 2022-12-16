from django.shortcuts import render, redirect, get_object_or_404
from ecommerceapp .models import product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request,'product.html')
def _cart_id_(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_to_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id_(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id_(request))

        cart.save()
    try:
        cart_item=CartItem.objects.get(product=prod,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=prod,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cartApp:cart_details')
def cart_details(request,total=0,counter=0,cart_items=None):

    try:

        cart=Cart.objects.get(cart_id=_cart_id_(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
             total +=(cart_item.product.price * cart_item.quantity)
             counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id_(request))
    produ = get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(product=produ,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartApp:cart_details')

def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id_(request))
    produ = get_object_or_404(product, id=product_id)
    cart_item = CartItem.objects.get(product=produ, cart=cart)
    cart_item.delete()
    return redirect('cartApp:cart_details')