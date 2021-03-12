from django.shortcuts import render

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

#def search(request):


def add(request):   
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    
    return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })    