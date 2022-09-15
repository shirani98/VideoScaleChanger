import ffmpeg
import os

def create_video_360(input_file_path:str) -> str:
    filename = os.path.basename(input_file_path)
    output_video_360_file_url = os.path.join('{}-360.mp4'.format(filename))
    output_video_360_path = os.path.join('media', f"{filename}-360.mp4")
    (
    ffmpeg
    .input(input_file_path)
    .filter("scale", w=360, h=360)
    .output(output_video_360_path)
    .run()
    )
    return output_video_360_file_url


def create_video_240(input_file_path:str) -> str:
    filename = os.path.basename(input_file_path)
    output_video_240_file_url = os.path.join('{}-240.mp4'.format(filename))
    output_video_240_path = os.path.join('media', f"{filename}-240.mp4")
    (
    ffmpeg
    .input(input_file_path)
    .filter("scale", w=240, h=240)
    .output(output_video_240_path)
    .run()
    )
    return output_video_240_file_url