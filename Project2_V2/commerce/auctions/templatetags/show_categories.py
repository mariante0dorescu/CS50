from django import template
from auctions.models import Category

register = template.Library()

@register.inclusion_tag("auctions/category_list.html")

def show_categories(categories):
    #categories = Category.objects.all()
    return {"categories": categories}
