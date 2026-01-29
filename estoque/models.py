from django.db import models

# Create your models here.

# Class item represents an item in the stock
class Item(models.Model): # Model é uma classe do Django na qual a nossa classe herda para o Django saber o que fazer.
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField(blank=True)

# Class Categoria represents a category of items
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, related_name='categorias')
