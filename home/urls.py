from django.urls import path
from .views import homepage, select_by_category, news_detail
urlpatterns = [
    path('', homepage, name='homepage'),
    path('categories/<category_id>/', select_by_category, name='select_by_category'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),


]