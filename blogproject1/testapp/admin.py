from django.contrib import admin
from testapp.models import Post,comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','status']
    list_filter=('status','author','publish',)
    search_fields=('title','body',)
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish',]
    prepopulated_fields={'slug':('title',)}
class commentAdmin(admin.ModelAdmin):
     list_display=['name','post','body','created','active']
     list_filter=('active','created')
     search_fields=('name','body')
admin.site.register(Post,PostAdmin)
admin.site.register(comment,commentAdmin)
