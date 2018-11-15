#!/usr/bin/python3
import os
import json
directorylist = input("Enter the directories for mapping permissions \t")
filedict = {}
dirdict = {}
for directory in directorylist.split():
    for curdir, subdir, subfile in os.walk(directory):
        for file in subfile:
            filepath = os.path.join(curdir,file)
            if os.path.exists(filepath):
                filestatus = os.stat(filepath)
                filepermission = oct(filestatus.st_mode)[-4:]
                print('The file {} has the permission {:5}'.format(filepath,filepermission))
                filedict [filepath] =  filepermission
        for dire in subdir:
            direpath = os.path.join(curdir,dire)
            if os.path.exists(direpath):
                direstatus = os.stat(direpath)
                direpermission = oct(direstatus.st_mode)[-4:]
                print('The directory {} has the permission {:5}'.format(direpath,direpermission))
                dirdict [direpath] = direpermission
with open('fileperm.json','w') as fp:
    json.dump(filedict, fp)
with open('dirperm.json','w') as dp:
    json.dump(dirdict, dp)
