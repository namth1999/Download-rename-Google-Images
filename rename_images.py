import os

path = './images/pig-from-above'
file_type = 'jpg'
files = os.listdir(path)
txt_list = []
txt_index_list = []
jpg_index = 0

for index, file in enumerate(files):
    if file_type in file:
        jpg_index = jpg_index + 1
        txt_list.append(file.replace(file_type, 'txt'))
        txt_index_list.append(jpg_index)
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(jpg_index).zfill(8), '.' + file_type])))

for index, file in enumerate(files):
    if 'txt' in file and file in txt_list:
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(txt_index_list[txt_list.index(file)]).zfill(8), '.txt'])))

