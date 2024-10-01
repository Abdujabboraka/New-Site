from django.shortcuts import render
from .models import Category, News

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, "index.html", context)

def select_by_category(request, category_id):
    news = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    context = {
        'categories': categories,
           'news': news,
    }
    return render(request, "index.html", context)

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, "news_detail.html", context)