from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def get_hot_product():
    return Product.objects.all().order_by('?').first()


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:2]
    return same_products


def main(request):
    return render(request, 'mainapp/index.html',
    context={'title': 'home', 'main_menu': [{'href': 'index', 'name': 'home'},

                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})


def products(request, pk=None):

    title = 'catalog'
    #categories = ProductCategory.objects.all()
    #basket = request.user.basket.all()[0] if request.user.is_authenticated else []

    if pk:
        if pk == '0':
            products = Product.objects.all()
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        context = {
            'title': title,
            #'cat_menu': categories,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/catalog.html', context)

    hot_product = get_hot_product()

    same_products = get_same_products(hot_product)

    context = {
        'title': 'products',
        #'cat_menu': categories,
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/hot_products.html', context)


def product(request, pk):

    title = 'product_detailes'
    context = {
        'title': title,
        #'cat_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }
    return render(request, 'mainapp/product_detailes.html', context)

def contact(request):
    return render(request, 'mainapp/contacts.html',
    context={'title': 'contacts'})


def showroom(request):
    return render(request, 'mainapp/showroom.html',
    context={'title': 'showroom'})

# Create your views here.
