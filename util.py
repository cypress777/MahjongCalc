from PIL import Image
import pillow_heif
import os

def heic_to_jpg(file_name: str, keep: bool):
    heif_file = pillow_heif.read_heif(file_name)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    new_file_name = file_name.strip(".HEIC") + ".jpg"
    print("converting: ", file_name, " to", new_file_name)
    image.save(new_file_name, format("png"))
    if not keep:
        os.remove(file_name)