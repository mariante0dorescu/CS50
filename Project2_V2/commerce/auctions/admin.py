from django.contrib import admin
from .models import *

# Register your models here.

class BidsAdmin(admin.ModelAdmin):
    list_display = ['user','listing', 'bid']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'listing', 'comment']



admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Watching)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Bid, BidsAdmin)
