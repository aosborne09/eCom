from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from cart.forms import ProductQtyForm

from .models import Product 

# Create your views here.

def all_products(request):
	products = Product.objects.filter(active=True)
	return render_to_response('products/all.html', locals(), context_instance=RequestContext(request))
	

def single_product(request, slug):
	add_product = ProductQtyForm()
	product = get_object_or_404(Product, slug=slug)
	return render_to_response('products/single.html', locals(), context_instance=RequestContext(request))