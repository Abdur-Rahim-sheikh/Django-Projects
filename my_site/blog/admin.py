from django.contrib import admin
from .models import Post,Author,Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","date")
    list_filter = ("author","tags","date")
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
