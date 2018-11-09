# Script to rename files of a folder, with slug like filenames

from slugify import slugify
import re
import os
import shutil

FOLDER_PATH = "/home/sergio/Dokumentuak/util-scripts/images"
os.chdir(FOLDER_PATH)

def slug_file_name(file_name):
    slugify(fileName.lower())

for file_name in os.listdir(FOLDER_PATH):
    name = os.path.splitext(file_name)[0]
    extension = os.path.splitext(file_name)[1]
    new_name = f'{slugify(name)}{extension.lower()}'
    print(new_name)
    shutil.move(os.path.join(os.getcwd(), file_name), new_name)