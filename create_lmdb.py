#!/usr/bin/env python
"""
Script to create lmdb-db's from the created dataset

__author__ = "Martin Lautenbacher"
__version__ = "0.1"
"""

import utilities

config_path = 'create_dataset.ini'
settings = utilities.CreateDatasetSettings(config_path)

utilities.create_lmdb(settings.caffe_root, settings.result_path + '64/test/',
        settings.result_path + '64/test/filelist.txt', 'flickr_64_test_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '64/train/',
        settings.result_path + '64/train/filelist.txt', 'flickr_64_train_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '256/test/',
        settings.result_path + '256/test/filelist.txt', 'flickr_256_test_lmdb')
utilities.create_lmdb(settings.caffe_root, settings.result_path + '256/train/',
        settings.result_path + '256/train/filelist.txt', 'flickr_256_train_lmdb')

