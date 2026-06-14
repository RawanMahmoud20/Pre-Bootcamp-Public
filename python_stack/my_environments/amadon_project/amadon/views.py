from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from django.db.models import Sum

def index(request):
    # Display all available products in the store
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'amadon/index.html', context)

def buy(request):
    if request.method == "POST":
        # 1. Get the product ID and quantity from the form
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        # 2. Fetch the product from the database (fully secure, we don't trust prices from the browser)
        product = get_object_or_404(Product, id=product_id)
        
        # 3. Calculate the total for the current order
        current_total = product.price * quantity
        
        # 4. Save the order to the database so we can calculate the cumulative total later
        Order.objects.create(product=product, quantity=quantity, total_price=current_total)
        
        # 5. Store the current order data in the session to display it once on the checkout page
        request.session['last_charge'] = float(current_total)
        
        # 6. The magic Redirect to prevent order duplication on page refresh
        return redirect('checkout')
    
    return redirect('index')

def checkout(request):
    # Calculate the cumulative total for all orders
    all_orders = Order.objects.aggregate(
        total_qty=Sum('quantity'),
        total_spent=Sum('total_price')
    )
    
    context = {
        'last_charge': request.session.get('last_charge', 0.00),
        'total_qty': all_orders['total_qty'] or 0,
        'total_spent': all_orders['total_spent'] or 0.00
    }
    return render(request, 'amadon/checkout.html', context)