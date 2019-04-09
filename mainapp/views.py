from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/index.html',
    context={'title': 'home', 'main_menu': [{'href': 'index', 'name': 'home'},

                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})


def products(request, pk=None):

    title = 'catalog'
    categories = ProductCategory.objects.all()
    basket = request.user.basket.all()
    if pk:
        if pk == '0':
            products = Product.objects.all()
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        context = {
            'title': title,
            'cat_menu': categories,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/catalog.html', context)

    same_products = Product.objects.all()

    context = {
        'title': title,
        'cat_menu': categories,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    return render(request, 'mainapp/contacts.html',
    context={'title': 'contacts'})



def showroom(request):
    return render(request, 'mainapp/showroom.html',
    context={'title': 'showroom'})

# Create your views here.
