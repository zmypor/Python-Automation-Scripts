# Python script to download images in bulk from a website
import requests
def download_images(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        images = response.json() # Assuming the API returns a JSON array of image URLs
        for index, image_url in enumerate(images):
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(f"{save_directory}/image_{index}.jpg", "wb") as f:
                    f.write(image_response.content)