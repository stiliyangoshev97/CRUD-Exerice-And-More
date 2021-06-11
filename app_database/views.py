from django.shortcuts import render, get_object_or_404, redirect
from app_database.models import Beat
from app_database.models import Person
from app_database.models import Book
from app_database.models import Label

from django.urls import reverse


from app_database import forms
from app_database.forms import BookForm

from django.views.generic import ListView

# Create your views here.



def index(request):
	return render(request, 'app_database/index.html')


def like(request):
	beat = get_object_or_404(Beat)
	is_liked = beat.is_liked

	beat.like()

	is_liked = beat.is_liked

	return render(request, 'app_database/index.html', context = {'key': beat.is_liked})


def unlike(request):
	beat = get_object_or_404(Beat)
	is_liked = beat.is_liked

	beat.unlike()

	is_liked = beat.is_liked

	

	return render(request, 'app_database/index.html', context = {'key': beat.is_liked})




def create_person(request):
	person = Person(first_name = 'John', last_name = 'Hulk', age=31)
	person.save()

	context = {'person': person}


	return render(request, 'app_database/created.html', context)


def update_person(request,pk):
	person = Person.objects.get(pk=pk)
	person.age = 36
	person.first_name = 'Concho'
	person.save()

	context = {'person': person}


	return render(request, 'app_database/updated.html', context)


def delete_person(request, pk):
	person = Person.objects.get(pk=pk)
	person.delete()

	context = {'person': person}

	return render(request, 'app_database/deleted.html', context)

def create_book(request):
	if request.method == 'GET':
		form = BookForm()
		context = {'form': form}
		return render(request, 'app_database/create_book.html', context)
	else:
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save()
			book.save()
			return redirect('index')


def update_book(request, pk):
	book = Book.objects.get(pk=pk)
	if request.method == 'GET':
		form = BookForm(instance=book)
		context = {'form': form, 'book': book}
		return render(request, 'app_database/update_book.html', context)
	else:
		form = BookForm(request.POST, instance = book)
		book = form.save()
		book.save()
		return redirect('index')


def books_list(request):
	book = Book.objects.all()
	context = {'books': book}

	return render(request, 'app_database/books_list.html', context)

def authors_list(request):
	authors = Book.objects.all()
	context = {'authors': authors}

	return render(request, 'app_database/authors_list.html', context)



def delete_book(request, pk):
	book = Book.objects.get(pk=pk)

	book.delete()
	context = {'book': book}

	return render(request, 'app_database/index.html', context)


# Create a calculator with forms

from app_database.forms import FormCalculator

def form_calculator(request):
	submitbutton = request.POST.get('submit')

	number_one = 0
	number_two = 0
	result = 0

	form = FormCalculator(request.POST or None)

	if form.is_valid():
		number_one = form.cleaned_data.get('number_one')
		number_two = form.cleaned_data.get('number_two')

		result = number_one * number_two
	


	context = {
	'submitbutton': submitbutton,
	'number_one': number_one,
	'number_two': number_two,
	'form': form,
	'result': result,
	}

	return render(request, 'app_database/form_calculator.html', context)


# Show books by chosen label




# Show books by chosen author which can be find in the URL (try to do it also with a form)

def books_by_author(request, author):
	books = Book.objects.filter(author = author)

	if request.method == 'GET':
		books = books.order_by('-id')
		context = {'books': books, 'author': author}
		return render(request, 'app_database/books_by_author.html', context)

	return redirect('index')


# Make like and unlike view

def book_like(request, pk):
	book = Book.objects.get(pk=pk)

	book.like_book(pk)
	book.save()

	return redirect('index')


def book_unlike(request, pk):
	book = Book.objects.get(pk=pk)

	book.unlike_book(pk)
	book.save()

	return redirect('index')



# Show liked books

from django.contrib import auth

def liked_books_list(request):
	liked_books = Book.objects.filter(Book.is_liked == True)

	context = {'liked_books': liked_books}

	return render(request, 'app_database/liked_books_list.html', context)


# Book information (Pages, Description, Label)
def book_information(request, pk):
	book = Book.objects.get(pk=pk)

	book_pages = book.pages
	book_description = book.description
	book_is_liked = book.is_liked


	context = {
	'book_pages': book_pages,
	'book_description': book_description,
	'book_is_liked': book_is_liked,
	'book': book
	}

	return render(request, 'app_database/book_information.html', context)

# Book increment pages











