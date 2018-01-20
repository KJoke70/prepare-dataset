#!/usr/bin/env python2
"""
Creates train and test sets from the FlickrLogos-47 dataset


__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import utilities
import cv2
import shutil
import os.path

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

print 'test_filelist:', len(test_filelist), 'items.'

with open(train_path + 'filelist.txt', 'r') as f:
    train_filelist = f.readlines()
train_filelist = [x.strip() for x in train_filelist]
for i in xrange(len(train_filelist)):
    train_filelist[i] = train_filelist[i][2:]

print 'train_filelist:', len(train_filelist), 'items.'

if os.path.exists(settings.result_path):
    shutil.rmtree(settings.result_path)

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

# create cropped and scaled images and write filelist
# test folder 
new_test_filelist = []
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
        filepath = utilities.create_result_path('', test_filelist[i], j)
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
            new_test_filelist.append(filepath + ' ' + str(data.classid) + '\n')
#    utilities.delete_if_exists(settings.result_path + '64/test/filelist.txt')
#    utilities.delete_if_exists(settings.result_path + '256/test/filelist.txt')
filelist64 = open(settings.result_path + '64/test/filelist.txt', 'w')
filelist256 = open(settings.result_path + '256/test/filelist.txt', 'w')
filelist64.writelines(new_test_filelist)
filelist64.close()
filelist256.writelines(new_test_filelist)
filelist256.close()

print 'new_test_filelist:', len(new_test_filelist), 'items.'

# train folder 
new_train_filelist = []
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
        filepath = utilities.create_result_path('', train_filelist[i], j)
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
            new_train_filelist.append(filepath + ' ' + str(data.classid) + '\n')
filelist64 = open(settings.result_path + '64/train/filelist.txt', 'w')
filelist256 = open(settings.result_path + '256/train/filelist.txt', 'w')
filelist64.writelines(new_train_filelist)
filelist64.close()
filelist256.writelines(new_train_filelist)
filelist256.close()

print 'new_train_filelist:', len(new_train_filelist), 'itmes.'

# make labels list
labels_file = settings.flickrlogos_path + '/className2ClassID.txt'
with  open(labels_file) as f:
    labels = f.readlines()

labels = [l[:l.find('\t')] for l in labels]
labels_new_file = open(settings.result_path + 'flickrlogos_labels.txt', 'w')
for item in labels:
    print>> labels_new_file, item
labels_new_file.close()

