from django.contrib import admin
from .models import Post, Image
from uploader.models import Uploader

# Register your models here.


class ImagesInLine(admin.StackedInline):
    model = Image
    extra = 0


class UploaderInLine(admin.StackedInline):
    model = Uploader
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields': ['title', 'body', 'posted']}),
    ]
    inlines = [ImagesInLine, UploaderInLine]
    list_display = ['title', 'posted']
    list_filter = ('posted',)


admin.site.register(Post, PostAdmin)
admin.site.register(Image)
