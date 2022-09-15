import pytest
from django.test import TestCase, override_settings
from pathlib import Path
from django.apps import apps
from django.core.files import File
import os
from video.utils import create_video_240
from redis import Redis

# Create your tests here.

@pytest.mark.django_db
def test_run_ffmpeg():
    Video = apps.get_model('video','Video')
    path_test_file = Path('media/testfiles/testfile.mp4')
    with path_test_file.open(mode='rb') as f:
        video = Video.objects.create(original_file=File(f))
    video.video_240 = create_video_240(video.original_file.path)
    assert os.path.exists(os.path.join('media', video.video_240.path))

@pytest.mark.django_db
@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
def test_upload_file_and_check_database():
    Video = apps.get_model('video','Video')
    path_test_file = Path('media/testfiles/testfile.mp4')
    with path_test_file.open(mode='rb') as f:
        video = Video.objects.create(original_file=File(f))
    assert video.video_240 is not None 
    assert video.video_360 is not None 
    assert video.original_file is not None

def test_check_redis_connection():
    redis_host = '127.0.0.1'
    r = Redis(redis_host, socket_connect_timeout=1)
    assert r.ping()
