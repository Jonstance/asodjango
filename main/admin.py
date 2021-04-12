from django.contrib import admin
from main.models import Blog


class BlogAdmin(admin.ModelAdmin):
   exclude = ['posted']
   prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Blog, BlogAdmin)
