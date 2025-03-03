from .config import IMAGE_FOLDER
import os

def get_images_qnt():
    images = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    return len(images)
