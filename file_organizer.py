import os
import shutil
import time


def check():
	sourcepath ="" # put your sourcepath here, e.g. C:/Users/name/Desktop/
	sourcefiles = os.listdir(sourcepath)
	python_path = "" # put your path to folder here, e.g. C:/Users/name/Desktop/folder_name
	javascript_path = "" #put your path to folder here, e.g. C:/Users/name/Desktop/folder_name
	java_path = "" # put your path to folder here, e.g. C:/Users/name/Desktop/folder_name
	for file in sourcefiles:
	    if file.endswith(""): # put the file extension name here
	        shutil.move(os.path.join(sourcepath,file), os.path.join(python_path,file))
	    elif file.endswith(""): # put the file extension name here
	        shutil.move(os.path.join(sourcepath,file), os.path.join(javascript_path,file))
	    elif file.endswith(""): # put the file extension name here
	        shutil.move(os.path.join(sourcepath,file), os.path.join(java_path,file))

while True:
	check()
	time.sleep(2)
