from django.db import models

from django.contrib.auth import get_user_model

from django.contrib import auth


User = get_user_model()
# Create your models here.

'''
from django.db import models
from django.urls import reverse


class Song(models.Model):
	title = models.TextField()
	artist = models.TextField()
	image = models.ImageField()
	audio_file = models.FileField(blank = True, null = True)
	audio_link = models.CharField(max_length = 200, blank = True, null = True)
	duration = models.CharField(max_length = 20)
	paginate_by = 2
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('App:b_detail', kwargs={'pk':self.pk})

	#def get_absolute_url(self):
		#return reverse('App:create')
'''


#user = models.ForeignKey(User,related_name='user_groups', on_delete = models.CASCADE)


class Beat(models.Model):
	user = models.ForeignKey(User, related_name = 'liked_beat', on_delete = models.CASCADE)
	title = models.CharField(max_length = 25)
	artist = models.CharField(max_length = 25)
	is_liked = models.BooleanField(default = False)


	def __str__(self):
		return self.title + ' by ' + self.artist


	def like(self):
		self.is_liked = True
		self.save()

	def unlike(self):
		self.is_liked = False
		self.save()



class Person(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	age = models.IntegerField()

	def __str__(self):
		return self.first_name


# Exercise to do

# Title, Pages, Desciption, Title

# One label can distribute one or more books <> one book can be distributed by one label

# Show liked books list

# Show books by chosen author = has to be done in views

# On book form make an attribute that can be incremented. Make a method in models and call it from views

class Book(models.Model):
	title = models.CharField(max_length = 30)
	pages = models.IntegerField()
	description = models.TextField(max_length = 100)
	author = models.CharField(max_length = 30)
	is_liked = models.BooleanField(default = False)
	


	def __str__(self):
		return self.title

	def increment_page(self, n):
		this.pages = this.pages + n

	def like_book(self, pk):
		self.is_liked = True

	def unlike_book(self, pk):
		self.is_liked = False

#user = models.ForeignKey(User,related_name='user_groups', on_delete = models.CASCADE)

class Label(models.Model):
	book_id = models.ForeignKey(Book, related_name='distributed_book', on_delete=models.CASCADE)
	name = models.CharField(max_length = 30)



	def __str__(self):
		return self.name















