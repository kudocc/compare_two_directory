#!/usr/bin/python

import sys
import os

#use python3

def get_all_files(rootDir, preLen):
    list = []
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            str = os.path.join(root, d)
            str = str[preLen:]
            list.append(str)
        for f in files:
            str = os.path.join(root, f)
            str = str[preLen:]
            list.append(str)
    return list

if len(sys.argv) != 3:
    print("argv should be 3 , python file and one for old directory , the other for new directory!")
    sys.exit(0)
fileOld = sys.argv[1]
preLenOld = len(fileOld)
fileNew = sys.argv[2]
preLenNew = len(fileNew)
listOld = get_all_files(fileOld, preLenOld)
listNew = get_all_files(fileNew, preLenNew)

setOld = set(listOld)
setNew = set(listNew)

print("old list size is", len(listOld))
print("new list size is", len(listNew))

for i in range(1, len(listOld)):
    if listOld[i] not in setNew:
        print(listOld[i] ,"is removed")
for i in range(1, len(listNew)):
    if listNew[i] not in setOld:
        print(listNew[i] ,"is added")
    else:
        filePath1 = fileOld + listNew[i]
        filePath2 = fileNew + listNew[i]
        fSize1 = os.path.getsize(filePath1)
        fSize2 = os.path.getsize(filePath2)
        if fSize1 != fSize2:
            print(listNew[i] ,"is modifyed, different file sizes")
        mtime1 = os.path.getmtime(filePath1)
        mtime2 = os.path.getmtime(filePath2)
        if mtime1 != mtime2:
            print(listNew[i], "is modifyed, modified times are different")


