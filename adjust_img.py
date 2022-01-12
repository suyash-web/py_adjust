import shutil
import os
import sys
from time import localtime
import progressbar
from PIL import Image

cwd = os.getcwd()
os.chdir(cwd)
def resize_images(original_folder, p_width, p_height):
    img_ext = [".png", ".PNG", ".jpeg", ".JPEG", ".bmp", ".BMP", ".GIF", ".gif"]
    folder = "resized_images "+str(p_width)+"pX"+str(p_height)+"p"
    shutil.copytree(original_folder, folder)
    count = 1
    li = []
    for i, j, k in os.walk(folder):
        for file in k:
            for ext in img_ext:
                if file.endswith(ext):
                    li.append(li)
    max = len(li)
    for dir, subdir, files in os.walk(folder):
       for filename in files:
            path = dir + os.sep + filename
            for ext in img_ext:
                if path.endswith(ext):
                    img = Image.open(path)
                    img = img.resize((int(p_height), int(p_width)), Image.ANTIALIAS)
                    img.save(path)
                    sys.stdout.write('\r')
                    sys.stdout.write(f"{int(100 * count/max)}%  Completed")
                    sys.stdout.flush()
                    count += 1
    print("\nDone.")
if __name__ == "__main__":
    #original_folder = cwd + "/Images"
    while True:
        files = input("Please provide the path to the directory.\nIf the folder is present in this directory then just type the folder's name:- ")
        if os.path.isdir(files) == False:
            print("Folder not found.")
            continue
        p_height = input("Pixel height:- ")
        p_width = input("Pixel width :- ")
        if p_height.isnumeric() == False or p_width.isnumeric() == False:
            print("Invalid input.")
            continue
        if p_height.isnumeric() == True and p_width.isnumeric() == True:
            print("Resizing...")
            break
    resize_images(files, p_height, p_width)
