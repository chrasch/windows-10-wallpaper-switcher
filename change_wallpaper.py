import os
import struct
import ctypes
import cProfile
from random import *
from PIL import Image

# Config Variables
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02
WALLPAPER_PATH = os.path.realpath('merged_image.jpg')
TOTAL_HEIGHT = 1920
TOTAL_WIDTH = 4920
PATH_IMG_HZ = '.\\1080p_hor\\'
PATH_IMG_VT = '.\\1080p_vert\\'
image_list = list()

def random_images():
   image_list_hz = list()
   image_list_vt = list()
   
   # Read the filenames in both directories
   for img_hz in os.listdir(PATH_IMG_HZ):
      image_list_hz.append(PATH_IMG_HZ + img_hz)
   for img_vt in os.listdir(PATH_IMG_VT):
      image_list_vt.append(PATH_IMG_VT + img_vt)
	  
   # Pick three random images and put them in a list. Superjanky!!
   hz_1 = sample(image_list_hz, 1)
   image_list.append(hz_1)
   hz_2 = sample(image_list_hz, 1)
   image_list.append(hz_2)
   vt_1 = sample(image_list_vt, 1)
   image_list.append(vt_1)

def merge_images():
   x_offset = 0
   y_offset = 0
   # Another janky crap. I hardcoded the coordinates for the pasting of the images. 
   # I'm shure you can do it better and i will redo it at some point.
   new_image = Image.new('RGB', (TOTAL_WIDTH, TOTAL_HEIGHT))
   for i in image_list:
      im = Image.open(i[0])
      if image_list.index(i) == 0:
         y_offset += int(1920/2) - int(im.height/2)
         x_offset = int(1920/2) - int(im.width/2)
         new_image.paste(im, (x_offset, y_offset))
         x_offset = 0
         y_offset = 0
      elif image_list.index(i) == 1:
         y_offset += int(1920/2) - int(im.height/2)
         x_offset = 3000 + int(1920/2) - int(im.width/2)
         new_image.paste(im, (x_offset, y_offset))
         x_offset = 0
         y_offset = 0
      elif image_list.index(i) == 2:
         y_offset += int(1920/2) - int(im.height/2)
         x_offset = 1920 + int(1080/2) - int(im.width/2)
         new_image.paste(im, (x_offset, y_offset))
         x_offset = 0
         y_offset = 0
   new_image.save('merged_image.jpg', 'JPEG')

def get_sys_parameters_info():
   # Only works with Windows 10 64 Bit!
   return ctypes.windll.user32.SystemParametersInfoW
   
def change_wallpaper():
   sys_parameters_info = get_sys_parameters_info()
   sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

random_images()
merge_images()
change_wallpaper()





