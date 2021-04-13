from django.contrib import admin
from main.models import Blog, Books


class BlogAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug', 'body','posted')
   search_fields = ['title', 'body']
   exclude = ['posted']
   prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Books)

