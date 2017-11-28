#!/usr/bin/env python
"""
Creates train and test sets from the FlickrLogos-47 dataset


__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import utilities
import cv2

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

# variable for

# create cropped images
# test folder 
for i in xrange(len(test_filelist)):
    info_path = test_path + utilities.get_info_file_path(test_filelist[i])
    with open(info_path, 'r') as f:
        info = f.readlines()
    info = [x.strip() for x in info]
    img = cv2.imread(test_path + test_filelist[i]) #load image
    for j in xrange(len(info)):
        data = utilities.ImageInfo(info[j])
        new_path_64 = utilities.create_result_path(settings.result_path +
                '64/test/', test_filelist[i], j)
        new_path_256 = utilities.create_result_path(settings.result_path +
                '256/test/', test_filelist[i], j)
        create = False
        if settings.ignore_difficult:
            if settings.ignore_truncated:
                if not data.difficult and not data.truncated:
                    create = True
            else:
                if not data.difficult:
                    create = True
        else:
            if settings.ignore_truncated:
                if not data.truncated:
                    create = True
            else:
                create = True
        if create:
            crop=utilities.crop_image(img, data.x1, data.y1, data.x2, data.y2)
            resized64 = utilities.scale(64, crop, 256)
            cv2.imwrite(new_path_64, resized64)
            resized256 = utilities.scale(256, crop, 256)
            cv2.imwrite(new_path_256, resized256)



# train folder 
for i in xrange(len(train_filelist)):
    info_path = train_path + utilities.get_info_file_path(train_filelist[i])
    with open(info_path, 'r') as f:
        info = f.readlines()
    info = [x.strip() for x in info]
    img = cv2.imread(train_path + train_filelist[i]) #load image
    for j in xrange(len(info)):
        data = utilities.ImageInfo(info[j])
        new_path_64 = utilities.create_result_path(settings.result_path +
                '64/train/', train_filelist[i], j)
        new_path_256 = utilities.create_result_path(settings.result_path +
                '256/train/', train_filelist[i], j)
        create = False
        if settings.ignore_difficult:
            if settings.ignore_truncated:
                if not data.difficult and not data.truncated:
                    create = True
            else:
                if not data.difficult:
                    create = True
        else:
            if settings.ignore_truncated:
                if not data.truncated:
                    create = True
            else:
                create = True
        if create:
            crop=utilities.crop_image(img, data.x1, data.y1, data.x2, data.y2)
            resized64 = utilities.scale(64, crop, 256)
            cv2.imwrite(new_path_64, resized64)
            resized256 = utilities.scale(256, crop, 256)
            cv2.imwrite(new_path_256, resized256)



