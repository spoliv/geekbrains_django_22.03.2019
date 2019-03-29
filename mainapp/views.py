from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html',
    context={'title': 'home', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})



def products(request):
    return render(request, 'mainapp/catalog.html',
    context={'title': 'catalog', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})


def contact(request):
    return render(request, 'mainapp/contacts.html',
    context={'title': 'contacts', 'main_menu': [{'href': 'index', 'name': 'home'},
                                            {'href': 'catalog', 'name': 'products'},
                                            {'href': 'contacts', 'name': 'contact'}
                                            ]})

# Create your views here.
