from django.shortcuts import render
from django.http import HttpResponse

from . import util

entries = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": entries
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


    