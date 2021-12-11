from PIL import Image
import os
from more_itertools import flatten
import time

def generate_gif(maps,factor,filepath,filename):
    """
    Args:
        maps (list): a list of maps of same size with values between 0 and 9
        factor (int): resizing factor
        filepath (str): path to store the gif
        filename (str): filename
    """
    # color picker: https://coolors.co/002626-0e4749-95c623-e55812-efe7da
    pixel_colors = {0: (255, 255, 102),
                    1: (33, 37, 41),
                    2: (52, 58, 64),
                    3: (73, 80, 87),
                    4: (108, 117, 125),
                    5: (173, 181, 189),
                    6: (222, 226, 230),
                    7: (233, 236, 239),
                    8: (248, 249, 250),
                    9: (255, 255, 255)
                   }
    img_list = []
    height = len(maps[0])*factor
    width = len(maps[0][0])*factor
    for m in maps:
        imap=[]
        for row in m:
            for _ in range(factor):
                imap.append(list(flatten([val]*factor for val in row)))

        im = Image.new("RGB", (width, height), "#FFFFFF")
        pixels = im.load()
        for y in range(0,height):
            for x in range(0,width):
                colors=pixel_colors.get(imap[y][x],(255,0,000))
                pixels[x,y] = colors
        img_list.append(im)
    
    # The display duration of each frame of the multiframe gif, in milliseconds. 
    # Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
    im.save(os.path.join(filepath,f"{filename}_{time.strftime('%H%M%S')}.gif"), 
        save_all=True, append_images=img_list, optimize=True, duration=100, loop=0)
    
