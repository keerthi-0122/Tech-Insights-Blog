from django.contrib import admin
from.models import Post,Category

# Register your models here.

class Post_admin(admin.ModelAdmin):
    list_display=('title','content')

    searh_fields=('title','content')
    
    list_filter=('category','created_at')





admin.site.register(Category)

admin.site.register(Post)
