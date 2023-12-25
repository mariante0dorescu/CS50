import re


from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def get_splitted_content(title):
    """
    Retrieves an encyclopedia entry by its filename with title and content separated. 
    If no such entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        file = f.read().decode("utf-8")
      
        lines = file.split('\n')
        #extract title
        title = lines[0][2:].strip()

        #extract the rest of the file
        content = "".join(lines[1:]).strip()

        return title, content
    
    except FileNotFoundError:
        return None, None