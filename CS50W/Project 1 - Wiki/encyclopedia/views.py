from django.shortcuts import render, redirect
from django.contrib import messages
import random, re
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, entry):
    entries = util.list_entries()
    if entry in entries:
        return render(request, "encyclopedia/content.html", {
        "content": util.get_entry(entry),
        "entry": entry
        })
    return render(request, "encyclopedia/entry_not_found.html", {
        "entry": entry
    } ,status=404)

def random_page(request):
    entry = random.choice(util.list_entries())
    return redirect("content", entry)

def query(request):
    q = request.GET.get('q')
    entries = util.list_entries()

    for entry in entries:
        if q.lower() == entry.lower():
            return redirect("content", entry)
    
    results = []
    for entry in entries:
        if re.search(q, entry, re.IGNORECASE):
            results.append(entry)
    
    return render(request, "encyclopedia/search.html", {
        "results": results
    })

def new_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('content')

        if not title:
            messages.error(request, "Error: Missing tittle")
            return render(request, "encyclopedia/new_entry.html")
        
        if not body:
            messages.error(request, "Error: not content body")
            return render(request, "encyclopedia/new_entry.html")

        if util.search_entry(title):
            messages.error(request, "Error: Entry already exist")
            return render(request, "encyclopedia/new_entry.html")
        else:
            util.save_entry(title, body)
            messages.success(request, "Success: Entry created")
            return redirect("content", title)

    else:
        return render(request, "encyclopedia/new_entry.html")