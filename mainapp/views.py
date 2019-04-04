from django.shortcuts import render
from .models import ProductCategory

def main(request):
    return render(request, 'mainapp/index.html',
    context={'title': 'home', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})



def products(request):
    categories = ProductCategory.objects.all()
    return render(request, 'mainapp/catalog.html',
    context={'title': 'catalog', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ],
             'cat_menu': categories
             })


def contact(request):
    return render(request, 'mainapp/contacts.html',
    context={'title': 'contacts', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})



def showroom(request):
    return render(request, 'mainapp/showroom.html',
    context={'title': 'showroom', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'showroom', 'name': 'showroom'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})

# Create your views here.
