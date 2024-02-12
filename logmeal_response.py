import os

import requests
from dotenv import load_dotenv
from fastapi import File, UploadFile

load_dotenv()

api_user_token = os.getenv("LOGMEAL_API")


async def logmeal_response(image: UploadFile = File(...)):
    headers = {"Authorization": "Bearer " + api_user_token}
    url = "https://api.logmeal.es/v2/image/segmentation/complete"
    resp = requests.post(
        url,
        files={"image": (image.filename, image.file, image.content_type)},
        headers=headers,
    )
    url = "https://api.logmeal.es/v2/recipe/ingredients"
    resp = requests.post(url, json={"imageId": resp.json()["imageId"]}, headers=headers)
    print(resp.json())
    return resp.json()
