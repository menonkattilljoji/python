#!/usr/bin/python3
import os
import subprocess
import json
with open('fileperm.json','r') as fp:
    filedict = json.load(fp)
with open('dirperm.json','r') as dp:
    dirdict = json.load(dp)
for fpath,fperm in filedict.items():
    subprocess.call(['chmod', fperm, fpath])
print("Completed restoration of file permissions")
for dpath,dperm in dirdict.items():
    subprocess.call(['chmod', dperm, dpath])
print("Completed restoring the directory permissions")
