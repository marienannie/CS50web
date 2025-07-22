from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    return render(request, "encyclopedia/add.html")

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f'The "{title}" entry does not exist.'
        })
    return render(request, "encyclopedia/entry.html"), {
        "title": title,
        "content": markdown2.markdown(content)
    }
