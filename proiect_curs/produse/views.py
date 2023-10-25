from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from .forms import ProductsForm

products = [

]

def home(request):

    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            products = Products.objects.all()
            context = {'form': form, 'products': products}
            return render(request, 'produse/home.html', context)
    else:
        form = ProductsForm()
        products = Products.objects.all()
        context = {'form': form, 'products': products}
        return render(request, 'produse/home.html', context)

def disponibilitate(request, disponibilitate):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            form = ProductsForm()
        return render(request, 'adauga_produs.html', {'form' : form})
def delete(reguest, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

def about(request):
    # return HttpResponse('<h2>About my app</h2>')
    return render(request, 'produse/about.html')
def adauga_produs(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            new_product = form.save(commit=False)
            #new_product.stoc_disponibil = form.cleaned_data['stoc_disponibil']
            #new_product.save()

    else:
        form = ProductsForm()

    return render(request, 'produse/adauga_produs.html', {'form': form})
