from django.shortcuts import render, redirect
import random
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
    