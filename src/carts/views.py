from django.shortcuts import render

# Create your views here.

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None: #and isinstance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 1
    else:
        print('Cart id exists')
    return render(request, "carts/home.html", {})