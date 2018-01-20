"""
Tools to turn the flickrlogos-47 dataset into a training/test set for DNN

__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import ConfigParser
import os
import cv2
import numpy as np
import subprocess

class CreateDatasetSettings:
    """ class to store settings for converting the flickrlogos-47
    classification dataset into a test/training dataset """

    default_file_path = 'create_dataset.ini'

    def __init__(self, path = default_file_path):
        """
        Constructor of CreateDatasetSettings
        Loads settings file or loads the defaults and writes those to disk if
        no settings file exists
        """
        if os.path.isfile(path):
            self.file_path = path
            try:
                config = ConfigParser.ConfigParser()
                config.read(path)
                self.caffe_root = config.get('Paths', 'caffe_root')
                if not self.caffe_root.endswith('/'):
                    self.caffe_root = self.caffe_root + '/'
                self.flickrlogos_path = config.get('Paths', 'flickrlogos_path')
                if not self.flickrlogos_path.endswith('/'):
                    self.flickrlogos_path = self.flickrlogos_path + '/'
                self.result_path = config.get('Paths', 'result_path')
                if not self.result_path.endswith('/'):
                    self.result_path = self.result_path + '/'
                self.ignore_difficult = config.get('Flags', 'ignore_difficult')
                self.ignore_truncated = config.get('Flags', 'ignore_truncated')
                self.use_size_threshold = config.get('Flags',
                        'use_size_threshold')
                self.size_threshold = config.get('Threshold',
                        'size_threshold')
            except:
                raise
        else:
            # default paths
            self.caffe_root = '../../caffe/'
            self.flickrlogos_path = '../../flickrlogos/'
            self.result_path = 'result_set/'
            # default flags
            self.ignore_difficult = True
            self.ignore_truncated = False
            self.use_size_threshold = True
            # thresholds
            self.size_threshold = 20

            self.write_settings()


    def write_settings(self, path = default_file_path):
        """ Writes settings to the file specified in path """
        file = open(path, 'w')
        config = ConfigParser.ConfigParser()
        config.add_section('Paths')
        config.add_section('Flags')
        config.add_section('Threshold')
        config.set('Paths', 'caffe_root', self.caffe_root)
        config.set('Paths', 'flickrlogos_path', self.flickrlogos_path)
        config.set('Paths', 'result_path', self.result_path)
        config.set('Flags', 'ignore_difficult', self.ignore_difficult)
        config.set('Flags', 'ignore_truncated', self.ignore_truncated)
        config.set('Flags', 'use_size_threshold', self.use_size_threshold)
        config.set('Threshold', 'size_threshold', self.size_threshold)
        config.write(file)

def crop_image(img, x1, y1, x2, y2):
    """ returns the cropped image specified by x1, y1, x2, y2 """
    return img[y1:y2, x1:x2]

def get_info_file_path(path):
    """
    example:
    path=/000001/000001493.png
    returns /000001/000001493.gt_data.txt
    """
    return path[:16] + '.gt_data.txt'

def makedirs(dir):
    """ creates dirs for a path if they don't exist """
    if not os.path.exists(dir):
        os.makedirs(dir)

def create_result_path(prefix, path, nr):
    """
    returns path for new file. prefix is e.g. '64/test/', path is e.g.
    '000000/000000144.png', nr is number of cropped image
    """
    return prefix + path[:-4] + '_'  + '{:04d}'.format(nr) + '.png'

class ImageInfo:
    """ Class to save info from *.gt_data.txt files """
    def __init__(self, path):
        s = path.split()
        self.x1 = int(s[0])
        self.y1 = int(s[1])
        self.x2 = int(s[2])
        self.y2 = int(s[3])
        self.classid = int(s[4])
        self.maskstring = s[6]
        self.difficult = bool(int(s[7]))
        self.truncated = bool(int(s[8]))


def scale(new_width, image, total_width):
    """
    scales image to new_width x new_width and adds borders to bloat the
    image to total_width x total_width
    uses INTER_NEAREST for scaling
    """
    w = image.shape[1]
    h = image.shape[0]
    if w > h:
        r = float(new_width) / w
        dim = (new_width, int(h * r))
    else:
        r = float(new_width) / h
        dim = (int(w * r), new_width)
    if r > 1.0:
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_CUBIC)
    else:
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #resized = cv2.resize(image, dim, interpolation = cv2.INTER_NEAREST)
    w_diff = total_width - resized.shape[1]
    h_diff = total_width - resized.shape[0]
    border_left = int(w_diff / 2)
    border_right = w_diff - border_left
    border_top = int(h_diff / 2)
    border_bottom = h_diff - border_top
    BLACK = [0, 0, 0]
    return cv2.copyMakeBorder(resized, border_top, border_bottom, border_left,
            border_right, cv2.BORDER_CONSTANT, value=BLACK)

def create_lmdb(caffe_root, path, listfile, db_name):
    """
    function to create lmdb from the images in path which are listed in the
    listfile
    """
    if caffe_root.endswith('/'):
        program_path = caffe_root + 'build/tools/convert_imageset'
    else:
        program_path = caffe_root + '/build/tools/convert_imageset'
    if path.endswith('/'):
        root_folder = path
    else:
        root_folder = path + '/'
    subprocess.call(program_path + ' ' + root_folder + ' ' + listfile + ' ' +
            db_name, shell = True)

