from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, entry):
    return render(request, "encyclopedia/content.html", {
        "content": util.get_entry(entry),
        "entry": entry
    })

