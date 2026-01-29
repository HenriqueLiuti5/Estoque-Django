from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

# Create your views here.
#Function to list all items in the databse and search for items
@login_required
def list_items(request):
    search_query = request.GET.get('search')

    if search_query:
        items = Item.objects.filter(nome__icontains=search_query)
    else:
        items = Item.objects.all().order_by('nome')
        
    return render(request, './estoque/home.html', {'items': items})

#Function to add a new item to the database
@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, './estoque/add_item.html', {'form': form})

#function to delete an item from the database
@login_required
def delete_item(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(id=item_id)
        item.delete()
    return redirect('home')

#function to edit an item in the database
@login_required
def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, './estoque/edit_item.html', {'form': form})