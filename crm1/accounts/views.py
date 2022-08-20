from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter

# Create your views here.

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    total_order = order.count()
    total_customer = customer.count()

    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {
        'order': order, 'customer': customer,
        'delivered': delivered, 'pending': pending,
        'total_customer': total_customer, 'total_order': total_order,

    }

    return render(request, 'accounts/deshboard.html',context)

def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/product.html',{'product': product})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    total_order = orders.count()

    myfilter = OrderFilter(request.POST, queryset=orders)
    orders = myfilter.qs
    context = {'customer': customer, 'orders': orders, 'total_order': total_order, 'myfilter':myfilter}


    return render(request, 'accounts/customer.html',context)


def createOrder(request, id):
    OrderFromSet = inlineformset_factory(Customer, Order,fields=('product','status'), extra=10)
    customer = Customer.objects.get(id=id)
    formset = OrderFromSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial= {'customer': customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFromSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
        
    context = {
        'formset': formset,
    }
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, id):
    
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)  #instance use for order data set to the form

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'order': order,
        }
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {
        'item': order,

    }

    return render(request, 'accounts/delete.html',context)
