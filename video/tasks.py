from django.utils import timezone
from video.utils import create_video_240, create_video_360
from .models import Video
from celery import shared_task

@shared_task
def change_scale_video(video_id:int):
    start_time = timezone.now()
    video = Video.objects.get(id = video_id)
    video.video_240 = create_video_240(video.original_file.path)
    video.video_360 = create_video_360(video.original_file.path)
    video.convert_time = timezone.now() - start_time
    video.save(update_fields=["video_240","video_360","convert_time"])
