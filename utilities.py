"""
Tools to turn the flickrlogos-47 dataset into a training/test set for DNN

__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import ConfigParser
import os

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
                self.flickrlogos_path = config.get('Paths', 'flickrlogos_path')
                if not self.flickrlogos_path.endswith('/'):
                    self.flickrlogos_path = self.flickrlogos_path + '/'
                self.result_path = config.get('Paths', 'result_path')
                if not self.result_path.endswith('/'):
                    self.result_path = self.result_path + '/'
                self.ignore_difficult = config.get('Flags', 'ignore_difficult')
                self.ignore_truncated = config.get('Flags', 'ignore_truncated')
            except:
                raise
        else:
            # default paths
            self.flickrlogos_path = '../../flickrlogos/'
            self.result_path = 'result_set/'
            # default flags
            self.ignore_difficult = True
            self.ignore_truncated = False
            self.write_settings()


    def write_settings(self, path = default_file_path):
        """ Writes settings to the file specified in path """
        file = open(path, 'w')
        config = ConfigParser.ConfigParser()
        config.add_section('Paths')
        config.add_section('Flags')
        config.set('Paths', 'flickrlogos_path', self.flickrlogos_path)
        config.set('Paths', 'result_path', self.result_path)
        config.set('Flags', 'ignore_difficult', self.ignore_difficult)
        config.set('Flags', 'ignore_truncated', self.ignore_truncated)
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
    return prefix + path[:-4] + '_'  + '{:02d}'.format(nr) + '.png'

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



