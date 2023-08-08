from django.contrib import admin
from .models import Contact,Post
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phoneNumber','message']
    

admin.site.register(Contact,ContactAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title']

admin.site.register(Post,PostAdmin)


#username srisudhatri
#password Sri@2022