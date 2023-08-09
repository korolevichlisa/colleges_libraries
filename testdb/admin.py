from django.contrib import admin

# Register your models here.

from .models import Coworkers, New, College, Library_funds, Library_room, Library_servic, Exhibition, Photos

# class PhotoAdmin(admin.StackedInline):
#     model = Photos

# class LessonAdmin(admin.ModelAdmin):
#     inlines = [PhotoAdmin]

#     class Meta:
#         model = Room

class PostImageAdmin(admin.StackedInline):
    model = Photos

@admin.register(Library_room)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Library_room

@admin.register(Photos)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(New)
admin.site.register(College)
admin.site.register(Coworkers)
admin.site.register(Library_funds)
# admin.site.register(Room)
admin.site.register(Library_servic)
admin.site.register(Exhibition)
# admin.site.register(Photos)


#super user admin pass:admin1     admin@ukr.net