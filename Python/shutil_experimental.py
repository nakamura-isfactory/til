#:basename:shutil_experimental.py

import os
import shutil

file1 = '/tmp/file1'
file2 = '/tmp/file2'
dir1 = '/tmp/dir1'
dir2 = '/tmp/dir2'
shutil.copy(file1, file2)
shutil.copytree(dir1, dir2)

shutil.copytree(file1, file2) # NotADirectoryError: [Errno 20] Not a directory: '/tmp/file1'
shutil.copy(dir1, dir2)
