from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.safestring import mark_safe

import markdown2
import secrets
from . import util


def index(request):
    '''
    check if the search query was submited by form via post
    and will filter the current titles by the search input value
    if exact match is found, it will redirect to the title page
    if no exact match is found, will return a list with 
    if not, a message is displayed and all the items are displayed
    '''
    if request.method == "POST":
        current_titles = util.list_entries()
        search_title = request.POST.get('q', '')
        exact_title = [title for title in current_titles if title.lower() == search_title.lower()]
        filtered_titles = [title for title in current_titles if search_title in title.lower()]
        #check exact tilte and redirect to the title page
        if(exact_title):
            return HttpResponseRedirect(reverse('encyclopedia:title', args=[exact_title[0]]))
        
        #returns a list with matching titles
        elif any(filtered_titles):
             return render(request, "encyclopedia/index.html", {
                "message":"Search results:",
                "entries": filtered_titles
                })
        # returns index page with a message an 
        else:
            return render(request, "encyclopedia/index.html", {
                "message": mark_safe("<h3>No titles found.</h3> <br> Maybe you want to <a href='" + reverse('encyclopedia:create') + "'>create</a> a new entry for <strong>" + search_title + "</strong>."),
                "entries": util.list_entries()
            })
    #renders the page with titles list
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    # get the content of the file usign util get_entry function
    context = util.get_entry(title)

    # check if the title exists
    if context is None:
        return render(request, "encyclopedia/not_found.html",{
            "title": title
        })         
    
    #renders the page with title and converts markdown to html
    else:
        html = markdown2.markdown(context)
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "context": html
        })

def create(request):

    if request.method == "POST":
        file_name = request.POST['title']
        content = request.POST['content']
        
        #check if the title already exists
        current_titles = util.list_entries()
        '''
        if title exists, a message is displayed and the form
        is prepopulated with the user input values
        so it can change the title and keep the text
        '''
        if file_name in current_titles:
            return render(request, "encyclopedia/create.html", {
                "title": file_name,
                "content": content,
                "message" : "The title already exists."
                })
        else:
            #add title to the markdown text and it save as local file, after redirect to the title page
            converted_to_markdown = f"# {file_name}\n\n{content}"
            util.save_entry(file_name, converted_to_markdown)
        return HttpResponseRedirect(reverse('encyclopedia:title', args=[file_name]))

    return render(request, "encyclopedia/create.html")

def edit_title(request, title):
    # get the content of the entry splitted in title / content
    splitted_content = util.get_splitted_content(title)

    """if the form is submited via post, 
    the new content is saved on the current title
     and the user is redirected to the title page
    """
    if request.method == "POST":
        new_content = request.POST['content']
        converted_to_markdown = f"# {splitted_content[0]}\n\n{new_content}"
        util.save_entry(title, converted_to_markdown)
        return HttpResponseRedirect(reverse('encyclopedia:title', args=[title]))

    # on initial load, the textarea is prepolated with title content
    return render(request, "encyclopedia/edit.html", {
            "title": splitted_content[0],
            "content": splitted_content[1]
        })

def random(request):
    # get list of all entries
    entries = util.list_entries()    
    # get a random entry
    entry = secrets.choice(entries)
    # returns the title function with the random title
    return HttpResponseRedirect(reverse('encyclopedia:title', args=[entry]))