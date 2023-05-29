import os

# folder path
dir_path = r'E:\backUp\Dissertation\DataSet\labels\Z'
new_num = '29'

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in get_files(dir_path):
    openFile = open(os.path.join(dir_path, file), "rt")
    new_str = ""
    for line in openFile:
        new_line = (line[0].replace(line[0], new_num) + line[1:])
        new_str += new_line
    openFile.close()

    file = open(os.path.join(dir_path, file), "wt")
    file.write(new_str)
    file.close()
