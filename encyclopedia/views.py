from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="New Title")
    content = forms.CharField(label="Adding Content")

entries = util.list_entries()

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": util.get_entry(title)
    })

def search(request):
    newEntriesList = []
    if request.method == "GET":
        title = request.GET.get('q')
        if title in entries :
            return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": util.get_entry(title)
            })
        else:
            for searchItem in entries:
                if title in searchItem:
                    newEntriesList.append(searchItem),
            return render(request, "encyclopedia/index.html", {
                "entries": newEntriesList
            })

def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            newEntry = util.save_entry(title, content)
            if newEntry:
                entries.append(newEntry)
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[title]))
            else:
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[None]))
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })

    return render(request, "encyclopedia/create.html", {
            "form": NewEntryForm()
    }) 
    