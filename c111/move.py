import os
import shutil
from_dir="C:/Users/ACER/Downloads"
to_dir="C:/Users/ACER/Downloads"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(extension)