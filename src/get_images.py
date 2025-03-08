import random
import requests
import os
from .config import IMAGE_FOLDER, API_KEY


def download_image(query: str):

    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    url = f"https://api.pexels.com/v1/search?query={query}&per_page=10"
    headers = {"Authorization": API_KEY}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["photos"]:
            random_image = random.choice(data["photos"])  
            image_url = random_image["src"]["original"]
            image_path = os.path.join(IMAGE_FOLDER, f"image_{query}.jpg")
            print(image_path)
            img_data = requests.get(image_url).content
        else:
            print("error: photo not found")
            return None
        with open(image_path, "wb") as img_file:
            img_file.write(img_data)
        
        print("retornou img")
        return image_path
    
    raise Exception(response.json())

def get_images_with_list(keywords:list):
    paths = []
    for k in keywords:
        if k:
            paths.append(download_image(k))
    print("deu bom")
    return paths