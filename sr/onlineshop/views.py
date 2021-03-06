from django.http import HttpResponse
from django.template import loader

from api.models import Category, Product


def index(request):
    
    categories = Category.objects.all()

    categories = Category.objects.order_by('-created')[:5]
    template = loader.get_template("onlineshop/index.html")
    categories_list=[]
    for cat in categories:
    	categories_list.append(cat.name)

    context = {
        'categories': categories,
        'categories_list':categories_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def add(request):
    return HttpResponse("Add ")