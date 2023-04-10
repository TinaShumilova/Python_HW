import os
from HW_7 import add_files as add
from HW_7 import rename as ren

TEMP = ['testqwerty.txt', 'dataqwerty.txt', 'exampleqwerty.pdf']

files_list = add.add_dir_with_files(TEMP)

ren.rename_file_name(files_list, "_TEST_", 3, "txt", "md", [1, 4])
