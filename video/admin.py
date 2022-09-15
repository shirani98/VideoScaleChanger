from django.contrib import admin

from video.models import Video

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ("video_240","video_360","convert_time","created_at")
    