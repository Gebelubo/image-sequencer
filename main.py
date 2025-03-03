from src.get_images import get_images_with_list
from src.create_video import create_video
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from src.util import get_images_qnt
from src.config import VIDEO_DURATION

app = FastAPI()

VIDEO_PATH = "video.mp4"

@app.get("/video")
async def get_video(keywords:str):
    keywords = keywords.split(' ')
    create_video(get_images_with_list(keywords), output_path='video', duration=VIDEO_DURATION/get_images_qnt())
    if not os.path.exists(VIDEO_PATH):
        return {"error": "video not found"}
    
    return FileResponse(VIDEO_PATH, media_type="video/mp4", filename="video.mp4")

