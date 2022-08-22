import os
cwd=os.getcwd()
print(cwd)
chdir=os.chdir('/Users/palankiumesh/Documents')
cwd=os.getcwd()
print(cwd)
path="/Users/palankiumesh/Documents"
os.mkdir(path,0775);