#Miguel Aliaga
#File Organizer Project
#Notes#
#End goal is to abe able to place this in any system and orgnize the system. 
#Still needs to use 'from pathlib import path' to make this multi OS
#As well there can be a better way to orgnize file ext by json file
#Can use'while' to run in background with sleep function but not neeed now.


import os
import shutil

image_format = ["jpg","png","jpeg","gif","webp","tiff","bmp","indd"]
doc_format = ["doc","docx","html","htm","odt","pdf","xls","xlsx","xltx","xlsm","ods","ppt","pptx","txt"]
audio_format = ["mp3","wav"]
video_format = ["mp4","m4p","m4v","wmv","avi","webm","mpv","ogg","flv","swf","avchd"]
app_format = ["dng","exe","iso","msi"]
zip_format = ["zip","z","7z","rar","tar","gz","rpn","pkg","deb","cab"]

dst_path = r"D:\Test" # or C:\Users\~~

#folders = ('/Documents'+'/Pictures'+'/Music'+'/Video'+'/Application'+'/Zip')
   
if not os.path.exists(dst_path + "/Pictures"):
   os.makedirs(dst_path + "/Pictures")
if not os.path.exists(dst_path + "/Documents"):
    os.makedirs(dst_path + "/Documents")
if not os.path.exists(dst_path + "/Music"):
    os.makedirs(dst_path + "/Music")
if not os.path.exists(dst_path + "/Video"):
    os.makedirs(dst_path + "/Video")
if not os.path.exists(dst_path + "/Application"):
    os.makedirs(dst_path + "/Application")
if not os.path.exists(dst_path + "/Zip"):
    os.makedirs(dst_path + "/Zip")

src_path = r"D:\Downloads"   #path of unorganized folder or can do  ("./") - this will list out all files and dir 
                        # r - is to run as a raw string
files = os.listdir(src_path)

for file in files:
    if os.path.isfile(file) and file !="file_organizer.py":
        ext = (file.split(".")[-1]).lower()   #split file name, -1 will focues on extension

        if not ext:
            pass
        elif ext in image_format:
            shutil.move(file,dst_path + "/Pictures")
        elif ext in doc_format:
            shutil.move(file,dst_path + "/Documents")
        elif ext in audio_format:
            shutil.move(file,dst_path + "/Music")   
        elif ext in video_format: 
            shutil.move(file,dst_path + "/Video")
        elif ext in app_format:
            shutil.move(file,dst_path + "/Application")
        elif ext in zip_format: 
            shutil.move(file,dst_path + "/Zip")
