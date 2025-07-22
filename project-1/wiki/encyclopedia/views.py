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
    raw_markdown = util.get_entry(title)
    if raw_markdown is None:
        return render(request, "encyclopedia/error.html", {
            "message": f'The "{title}" entry does not exist.'
        })
    
    lines = raw_markdown.split('\n', 1)
    content_body = lines[1] if len(lines) > 1 else ''

    html_content = markdown2.markdown(content_body)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })
