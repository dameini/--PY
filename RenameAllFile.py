import os

path = 'E:\Project\TestPy\ShufaTiqu\liu'
num= 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,str(num)+".jpg"))
    num+=1
path = 'E:\Project\TestPy\ShufaTiqu\liu2'
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(num) + ".jpg"))
    num += 1
path = 'E:\Project\TestPy\ShufaTiqu\ou'
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(num) + ".jpg"))
    num += 1
path = 'E:\Project\TestPy\ShufaTiqu\ou2'
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, str(num) + ".jpg"))
    num += 1
