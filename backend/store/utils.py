from django.core.files import File
from pathlib import Path
from io import BytesIO
from PIL import Image


IMAGE_EXT = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
}


def image_resize(image, width, height):

    img = Image.open(image)
    if img.width > width or img.height > height :
        imgOutput_size = (width, height)
        img.thumbnail(imgOutput_size)
        img_filename = Path(image.file.name).name
        img_suffix =  Path(image.file.name).name.split('.')[-1]
        img_format = IMAGE_EXT[img_suffix]
        buffer = BytesIO()
        img.save(buffer, format = img_format)
        file_object = File(buffer)
        img.save(img_filename, file_object)
