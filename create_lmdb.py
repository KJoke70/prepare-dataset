#!/usr/bin/env python2
"""
Script to create lmdb-db's from the created dataset. This only calls the caffe programs to do so.

__author__ = "Martin Lautenbacher"
__version__ = "1.0"
"""

import utilities

config_path = 'create_dataset.ini'
settings = utilities.CreateDatasetSettings(config_path)

utilities.create_lmdb(settings.caffe_root, settings.result_path + '64/test/',
        settings.result_path + '64/test/filelist.txt', settings.result_path +
        '64/train/flickr_64_test_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '64/train/',
        settings.result_path + '64/train/filelist.txt', settings.result_path +
        '64/test/flickr_64_train_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '256/test/',
        settings.result_path + '256/test/filelist.txt', settings.result_path +
        '256/test/flickr_256_test_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '256/train/',
        settings.result_path + '256/train/filelist.txt', settings.result_path +
        '256/train/flickr_256_train_lmdb')

