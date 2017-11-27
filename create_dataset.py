#!/usr/bin/env python
"""
Creates train and test sets from the FlickrLogos-47 dataset


__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import utilities

# load config
config_path = 'create_dataset.ini'
settings = utilities.CreateDatasetSettings(config_path)

# paths
test_path = settings.flickrlogos_path + 'test/'
train_path = settings.flickrlogos_path + 'train/'

# filelists
with open(test_path + 'filelist.txt', 'r') as f:
    test_filelist = f.readlines()
test_filelist = [x.strip() for x in test_filelist]
for i in xrange(len(test_filelist)):
    test_filelist[i] = test_filelist[i][2:]

with open(train_path + 'filelist.txt', 'r') as f:
    train_filelist = f.readlines()
train_filelist = [x.strip() for x in train_filelist]
for i in xrange(len(train_filelist)):
    train_filelist[i] = train_filelist[i][2:]

# create folder structure for result 256x256 and 64x64 variant
utilities.makedirs(settings.result_path + '256/test/000000/')
utilities.makedirs(settings.result_path + '256/test/000001/')
utilities.makedirs(settings.result_path + '256/test/000002/')
utilities.makedirs(settings.result_path + '256/train/000000/')
utilities.makedirs(settings.result_path + '256/train/000001/')
utilities.makedirs(settings.result_path + '256/train/000002/')
utilities.makedirs(settings.result_path + '64/test/000000/')
utilities.makedirs(settings.result_path + '64/test/000001/')
utilities.makedirs(settings.result_path + '64/test/000002/')
utilities.makedirs(settings.result_path + '64/train/000000/')
utilities.makedirs(settings.result_path + '64/train/000001/')
utilities.makedirs(settings.result_path + '64/train/000002/')

