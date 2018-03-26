# prepare-dataset
The files provided are:
 * create_dataset.py
 * create_lmdb.py
 * divide_by_classes.py
 * utilities.py
 * create_dataset.ini

# create_dataset.ini
Settings file: is generated automatically if missing.
caffe_root and flickrlogos_path have to be adjusted to suit your setup.

| flag             | default            | explanation                                        |
| ---------------- | ------------------ | -------------------------------------------------- |
| caffe_root       | ../../caffe/       | path to root folder of compiled caffe framework    |
| flickrlogos_path | ../../flickrlogos/ | path to root of flickrlogos-47 dataset             |
| result_path      | result_set         | output folder; will be created                     |
| ignore_difficult | True               | snippets marked as 'difficult' are ignored if True |
| ignore_truncated | False              | snippets marked as 'truncated' are ignored if True |
| size_threshold   | 20                 | snippets with height + width <= 20 will be ignored |


# create_dataset.py
Creates 2 test and train datasets, with image sizes 256x256 and 64x64, suited for CNN classification.

This script reads the images from the flickrlogos-47 dataset, crops out snippets according to the bounding boxes provided in the dataset's `*.gt_data.txt` files. Snippets marked as 'difficult' or 'truncated' will be ignored depending on the `create_dataset.ini`. Snippets with `height + width <= size_threshold` will be ignored as well.

These snippets will then be scaled with the longer side matching 256 / 64 pixels and filled with black to reach 256x256 / 64x64

# create_lmdb.py
Calls the caffe tool `caffe/build/tools/convert_imageset` to turn the datasets created with `create_dataset.py` into lmdb databases.

#divide_by_classes.py
Copies the images from `result_set/256/test/` (created by `create_dataset.py`) into folders corresponding to their classification class.

# utilities.py
Functions and classes needed for the other scripts.
