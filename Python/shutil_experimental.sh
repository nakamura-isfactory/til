file1='/tmp/file1'
file2='/tmp/file2'
dir1='/tmp/dir1'
dir2='/tmp/dir2'
mkdir -p $dir1
echo aaa > $file1
rm -rf $file2 $dir2
python shutil_experimental.py
ls -l $file2
ls -ld $dir2
