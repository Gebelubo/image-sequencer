import os
import shutil
from moviepy import ImageSequenceClip
from .resize import resize_images_to_smallest

def create_video(image_paths, output_path='video', duration:int=20, archive_folder='archive'):
    print('paths')
    print(image_paths)

    if os.path.exists(output_path):
        os.remove(output_path)

    resize_images_to_smallest(image_paths=image_paths)

    clip = ImageSequenceClip(image_paths, durations=[duration] * len(image_paths))
    print("video criado")
    
    clip.write_videofile(output_path + '.mp4', fps=24)
    
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    for image_path in image_paths:
        try:
            image_name = os.path.basename(image_path)
            destination = os.path.join(archive_folder, image_name)
            shutil.move(image_path, destination)
        except Exception as e:
            print(f"Error {image_path}: {e}")

