from django.db import models



# Create your models here.
def get_upload_path():
    return "original_file"

class Video(models.Model):
    original_file = models.FileField(upload_to=get_upload_path())
    video_240 = models.FileField(upload_to=get_upload_path(),null=True,blank=True)
    video_360 = models.FileField(upload_to=get_upload_path(),null=True,blank=True)
    convert_time = models.CharField(max_length=100,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        from video.tasks import change_scale_video
        adding_state = self._state.adding
        super().save(*args, **kwargs)
        if adding_state:
            
            change_scale_video.delay(self.id)
    
    def __str__(self) -> str:
        return f"{self.original_file.name} video"
    