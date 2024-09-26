from cloudinary import CloudinaryImage
from django.contrib import admin
from .models import Course
from django.utils.html import format_html

# admin.site.register(Course)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj, *args, **kwargs):
        url = obj.image_admin_url
        # cloudinary_id = str(obj.image)
        # cloudinary_html = CloudinaryImage(cloudinary_id).image(width=400)
        return format_html(f"<img src={url} />")
    
    display_image.short_description = "Current image."