import os
import sys
import shutil

files_list = []

def import_list(file_list, raw_type):
    global files_list
    count = 0
    Lines = file_list.readlines()
    for line in Lines:
        temp = line.strip() + raw_type
        count += 1
        files_list.append(temp)
    if count == 0:
        raise Exception("No lines in provided file!")
    print("Found %s file names in file provided" % str(count))
    
def sort_folder(name_of_destination):
    global files_list
    count = 0
    source = os.getcwd()
    try:
        os.mkdir(name_of_destination)
        os.chdir(name_of_destination)
        destination = os.getcwd()
        print("Folder created at %s" % str(destination))
    except FileExistsError:
        os.chdir(name_of_destination)
        destination = os.getcwd()
        print("Folder moved to %s" % str(destination))
    os.chdir(source)
    files = os.listdir()
    if len(files) <= 3:
        raise Exception("No image files present!")
    for i in files:
        curr_file = os.path.join(os.getcwd(),i)
        file_name = os.path.basename(curr_file)
        if file_name in files_list:
            shutil.copy2(i, destination)
            print("Moved file %s" % (file_name))
            count += 1
        if count >= len(files_list):
            print("Moved %s files to folder %s" % (str(count), str(destination)))
            return
    if count == 0:
        raise Exception("Found none of the files that were provided in the file list!")
def main():
    if (len(sys.argv) <= 4)&(len(sys.argv) > 1):
        destination = str(sys.argv[1])
        file_list = str(sys.argv[2])
        raw_type = str(sys.argv[3])
    else:
        raise Exception("Please provide command line input as follows:\n python3 main.py DESTINATION_FOLDER_NAME FILE_LIST.txt RAW_TYPE")
    try:
        file = open(file_list)
    except:
        raise Exception("Could not find the file list")

    import_list(file, raw_type)
    sort_folder(destination)
    
main()