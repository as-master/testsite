from django.contrib import admin
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at','updated_at','is_published',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', )
    list_editable = ('is_published',)


admin.site.register(News, NewsAdmin)