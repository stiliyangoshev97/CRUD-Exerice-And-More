"""databases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_database import views

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('like/', views.like, name = 'like'),
    #url(r'^(?P<pk>\d+)/like$', views.like, name='like'),
    path('unlike/', views.unlike, name = 'unlike'),
    path('create/', views.create_person, name = 'create'),
    url(r'^update/(?P<pk>\d+)/$', views.update_person, name = 'update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_person, name = 'delete'),
    path('create_book/', views.create_book, name = 'create_book'),
    url(r'^update_book/(?P<pk>\d+)/$', views.update_book, name = 'update_book'),
    url(r'^delete_book/(?P<pk>\d+)/$', views.delete_book, name = 'delete_book'),
    path('books_list/', views.books_list, name = 'books_list'),
    path('calculator/', views.form_calculator, name = 'form_calculator'),
    # Show books by chosen author which can be find in the URL
    path('booksbyauthor/<author>/',views.books_by_author, name = 'books_by_author'),
    path('authors_list/', views.authors_list, name = 'authors_list'),
    url(r'^book_information/(?P<pk>\d+)/$', views.book_information, name = 'book_information'),
    url(r'^book_like/(?P<pk>\d+)/$', views.book_like, name = 'book_like'),
    url(r'^book_unlike/(?P<pk>\d+)/$', views.book_unlike, name = 'book_unlike'),
    path('liked_books_list/', views.liked_books_list, name = 'liked_books_list'),



]
