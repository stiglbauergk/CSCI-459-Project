from django.shortcuts import render, redirect
from animals.forms import AnimalForm
from animals.models import Animal


# Create your views here.
def animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                pass

    else:
        form = AnimalForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    animals = Animal.objects.all()
    return render(request, "show.html", {'animals': animals})


def edit(request, id):
    animals = Animal.objects.get(id=id)
    return render(request, 'edit.html', {'animals': animals})


def update(request, id):
    animals = Animal.objects.get(id=id)
    form = AnimalForm(request.POST, instance=animals)
    if form.is_valid():
        form.save()
        return redirect("")
    return render(request, 'edit.html', {'animals': animals})


def delete(request, id):
    animals = Animal.objects.get(id=id)
    animals.delete()
    return redirect("")
