from django.shortcuts import render, redirect
from .models import Item
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

def homepage(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm()

    items = Item.objects.all()
    return render(request, 'home.html', {'form': form, 'items': items})
