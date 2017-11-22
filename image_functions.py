"""
Functions to load, crop and scale images


__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

def crop_image(img, x1, y1, x2, y2):
    return img[y1:y2, x1:x2]


