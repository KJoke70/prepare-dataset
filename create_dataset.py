#!/usr/bin/env python
"""
Creates train and test sets from the FlickrLogos-47 dataset


__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import image_functions as imf
import settings as config

# load config
config_path='create_dataset.ini'
settings = config.CreateDatasetSettings(config_path)
