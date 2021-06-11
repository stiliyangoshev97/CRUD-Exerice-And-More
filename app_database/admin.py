from django.contrib import admin


from app_database.models import Beat
from app_database.models import Person
from app_database.models import Book
from app_database.models import Label

# Register your models here.

admin.site.register(Beat)
admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Label)