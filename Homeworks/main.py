import os
from HW_8 import read_dir as r

print("-------------")
dir_list = os.listdir()
temp_dict = r.look_into_dir(dir_list)
r.write_into_json(temp_dict, "test.json")
print("-------------")