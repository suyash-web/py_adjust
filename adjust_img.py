import shutil
import os
from PIL import Image

cwd = os.getcwd()
os.chdir(cwd)
def resize_images(p_width, p_height):
    folder = "resized_images "+str(p_width)+"pX"+str(p_height)+"p"
    shutil.copytree(original_folder, folder)
    for dir, subdir, files in os.walk(folder):
        for filename in files:
            path = dir + os.sep + filename
            if path.endswith(".png"):
                img = Image.open(path)
                img = img.resize((p_height, p_width), Image.ANTIALIAS)
                img.save(path)
if __name__ == "__main__":
    original_folder = cwd + "/Images"
    resize_images(600, 600)
    resize_images(1500, 1500)