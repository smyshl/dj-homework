from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_field = 'id'

    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        sort_field = 'name'
    elif sort_param == 'min_price':
        sort_field = 'price'
    elif sort_param == 'max_price':
        sort_field = '-price'

    phone_objects = Phone.objects.all().order_by(sort_field)
    context = {
        'phones': [
            {
                'name': i.name, 'price': i.price, 'image': i.image, 'release_date': i.release_date,
                'lte_exists': i.lte_exists, 'slug': i.slug} for i in phone_objects
        ]
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone_objects = Phone.objects.filter(slug=slug)[0]

    context = {
        'phone': {
                'name': phone_objects.name, 'price': phone_objects.price, 'image': phone_objects.image,
                'release_date': phone_objects.release_date, 'lte_exists': phone_objects.lte_exists, 'slug': phone_objects.slug
        }
    }
    return render(request, template, context)
