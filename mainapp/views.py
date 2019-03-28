from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', context={'title': 'home'})


def products(request):
    return render(request, 'mainapp/catalog.html', context={'title': 'catalog'})


def contact(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'contacts'})

# Create your views here.
