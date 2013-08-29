#!/usr/bin/python
from __future__ import print_function

import sys
import os
import shutil


def copy_models(src, dst):
     
    list_dir = [os.path.join(src,x) for x in os.listdir(src)]
    sub_dirs = [x for x in list_dir if os.path.isdir(x)]
    for model_path in sub_dirs:
        if 'model.config' in os.listdir(model_path):
            # sys.stdout.write(" copying %s" % model_path)
            print (".", end="")
            dest_dir = os.path.join(dst, os.path.split(model_path)[1] )
            shutil.copytree(model_path, dest_dir)
        else:
            print (" %s ignored" % model_path)
        

dest_dir = sys.argv[1]
print("copying local models to %s" % dest_dir)
gazebo_path =  os.environ['GAZEBO_MODEL_PATH'].split(':')
model_paths = [x for x in gazebo_path if os.path.isdir(x)]
unique_pahts = list(set(model_paths))
 
for path in unique_pahts:
    print("\npath: [%s]" % path)
    copy_models(path, dest_dir)
        