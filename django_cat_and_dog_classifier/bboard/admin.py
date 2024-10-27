from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title',)
    search_fields = ('title', 'content','price')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)