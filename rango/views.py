from django.shortcuts import render

from rango.models import Category
from rango.models import Page


def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]

    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', 'categories': categories, 'pages': pages}

    return render(request, 'rango/index.html', context=context)


def about(request):
    name = "xxx"
    message = f"This tutorial has been put together by {name}"
    return render(request, "rango/about.html", context={"message": message})


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
