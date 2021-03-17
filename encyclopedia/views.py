from django.shortcuts import render
from django.http import HttpResponse

from . import util


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
    if request.method == "GET":
        title = request.GET.get('q')
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": util.get_entry(title)
        })
    