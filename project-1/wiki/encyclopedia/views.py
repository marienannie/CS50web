from django.shortcuts import redirect, render
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    if (request.method == "POST"):
        title = request.POST["title"]
        content = request.POST["content"]

        all_entries = util.list_entries()

        for entry in all_entries:
            if entry.lower() == title.lower():
                return render(request, "encyclopedia/add.html", {
                    "title_input": title,
                    "content_input": content
                })
            
        full_content = f"# {title}\n\n{content}"

        util.save_entry(title, full_content)

        return redirect("entry", title=title)
    return render(request, "encyclopedia/add.html")

def entry(request, title):
    raw_markdown = util.get_entry(title)
    if raw_markdown is None:
        return redirect('error')
    
    lines = raw_markdown.split('\n', 1)
    content_body = lines[1] if len(lines) > 1 else ''

    html_content = markdown2.markdown(content_body)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)

def error(request):
    return render(request, "encyclopedia/error.html")

def search(request):
    query = request.GET.get("q", "").strip()
    all_entries = util.list_entries()

    for entry in all_entries:
        if query.lower() == entry.lower():
            return redirect("entry", title=entry)

    results = [entry for entry in all_entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/results.html", {"query":query, "results": results})

def edit(request, title):
    if request.method == "POST":
        action = request.POST.get("action")
        content = request.POST.get("content")

        if action == "save":
            full_content = f"# {title}\n\n{content}"
            util.save_entry(title, full_content)
            return redirect("entry", title=title)
        elif action == "delete":
            util.delete_entry(title)
            return redirect("index")
        
    raw_markdown = util.get_entry(title)
    if raw_markdown is None:
        return redirect('error')
    
    lines = raw_markdown.split('\n', 1)
    content_body = lines[1] if len(lines) > 1 else ''

    return render(request, "encyclopedia/edit.html", {
        "title_input": title,
        "content_input": content_body
    })