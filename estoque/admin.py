from django.contrib import admin
from .models import Item, Categoria
# Register your models here.

#Registering the models to show up in the admin interface
admin.site.register(Item)
admin.site.register(Categoria)