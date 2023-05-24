import os
folder_path = "img" 
file_list = os.listdir(folder_path)
jpg_files = [file for file in file_list if file.lower().endswith(".jpg")]
formatted_files = ['"' + file + '"' for file in jpg_files]
for file in formatted_files:
    print(file, end=",")
