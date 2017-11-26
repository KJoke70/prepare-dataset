"""
Class to store settings for creating the dataset

__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import ConfigParser
import os.path

class CreateDatasetSettings:
    """ class to store settings for converting the flickrlogos-47
    classification dataset into a test/training dataset """

    default_file_path = 'create_dataset.ini'

    def __init__(self, path = default_file_path):
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
            self.result_path = 'result_set'
            # default flags
            self.ignore_difficult = True
            self.ignore_truncated = False
            self.write_settings()


    def write_settings(self, path = default_file_path):
        file = open(path, 'w')
        config = ConfigParser.ConfigParser()
        config.add_section('Paths')
        config.add_section('Flags')
        config.set('Paths', 'flickrlogos_path', self.flickrlogos_path)
        config.set('Paths', 'result_path', self.result_path)
        config.set('Flags', 'ignore_difficult', self.ignore_difficult)
        config.set('Flags', 'ignore_truncated', self.ignore_truncated)
        config.write(file)

