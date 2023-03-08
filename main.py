import os
import sys
import shutil
import PySimpleGUI as sg

files_list = []

def check_file(file_name, window):
    try:
        file = open(file_name)
        window['-ERROR-'].update("")
        return file
    except:
        window['-ERROR-'].update("ERROR: Could not find the file list")
        return
        # sg.popup_error("Could not find the file list")

def import_list(file_list, raw_type, window):
    global files_list
    count = 0
    Lines = file_list.readlines()
    for line in Lines:
        temp = line.strip() + raw_type
        count += 1
        files_list.append(temp)
    if count == 0:
        window['-ERROR-'].update("ERROR: No lines in provided file!")
    else:
        window['-ERROR-'].update("")
    print("Found %s file names in file provided" % str(count))
    return count
    
def sort_folder(source, name_of_destination, window, percent):
    global files_list
    count = 0
    curr_progress = 0
    try:
        os.chdir(source)
        source = os.getcwd()
    except FileNotFoundError:
        window['-ERROR-'].update("ERROR: Folder not exsisting!")
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
        window['-ERROR-'].update("ERROR: No image files present!")
    else:
        window['-ERROR-'].update("")
    for i in files:
        curr_file = os.path.join(os.getcwd(),i)
        file_name = os.path.basename(curr_file)
        if file_name in files_list:
            shutil.copy2(i, destination)
            print("Moved file %s" % (file_name))
            curr_progress += percent
            window['progressbar'].UpdateBar(curr_progress)
            count += 1
        if count >= len(files_list):
            print("Moved %s files to folder %s" % (str(count), str(destination)))
            return
    if count == 0:
        window['-ERROR-'].update("ERROR: Found none of the files that were provided in the file list!")
    else:
        window['-ERROR-'].update("")


def window_setup():
    sg.theme('SystemDefaultForReal')

    layout = [
        [sg.Text('Enter the name of the .txt that holds the list of image names'), sg.InputText(key = 'FILE', do_not_clear = False), sg.FileBrowse()],
        [sg.Text("Enter the RAW file type for your images"), sg.InputText(key = 'RAW',do_not_clear = False)],
        [sg.Text('Enter the name of the folder in which these images are in'), sg.InputText(key = 'SOURCE', do_not_clear = False), sg.FolderBrowse()],
        [sg.Text('Enter the name of the folder in which you would want to store these images'), sg.InputText(key = 'DESTINATION', do_not_clear = False), sg.FolderBrowse()],
        [sg.Button('Submit'), sg.Button('Exit')],
        [sg.Text(size = (50,1), key = '-ERROR-', text_color='red'),sg.Text(size = (50,1), key = '-COMPLETE-', text_color='green')],
        [sg.Text('Program output:')],
        [sg.ProgressBar(1000, orientation = 'h', size = (20,20),  key = 'progressbar')],
        [sg.Text(size=(80,3), key='-COMMAND LINE-', text_color='yellow', font='Courier 8')],
        [sg.MLine(size=(80,10), reroute_stdout=True, reroute_stderr=True, reroute_cprint=True, write_only=True, font='Courier 8', autoscroll=True, key='-ML-')],
    ]
    window_post(layout)

def window_post(window_layout):
    window = sg.Window("Photo Sifter", window_layout, finalize = True)
    global files_list
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if len(values['FILE']) == 0 and len(values['RAW']) == 0 and len(values['DESTINATION']) == 0 and len(values['SOURCE']) == 0:
            window['-ERROR-'].update("ERROR: Please input every text field")
        elif len(values['FILE']) == 0 or len(values['RAW']) == 0 or len(values['DESTINATION']) == 0 or len(values['SOURCE']) == 0:
            if len(values['FILE']) == 0:
                window['-ERROR-'].update("ERROR: File name is not included")
            elif len(values['RAW']) == 0:
                window['-ERROR-'].update("ERROR: RAW file type is not included")
            elif len(values['DESTINATION']) == 0:
                window['-ERROR-'].update("ERROR: Destination folder is not included")
            elif len(values['SOURCE']) == 0:
                window['-ERROR-'].update("ERROR: Source folder is not included")
        else:
            window['-ERROR-'].update("")
            file = values['FILE']
            raw = values ['RAW']
            source = values ['SOURCE']
            destination = values ['DESTINATION']
            file = check_file(file, window)
            if file is not None:
                count = import_list(file, raw, window)
                percent = 1000/count
                window.perform_long_operation(lambda: sort_folder(source, destination, window, percent), '-FUNCTION COMPLETE-')
                event, values = window.read()
            if event == '-FUNCTION COMPLETE-':
                files_list = []
                sg.popup_ok("Service Completed!")

                # window.close()
                # window_setup()

    window.close()

def main():

    window_setup()

    # filename = sg.popup_get_file("Enter the name of the .txt that holds the list of image names")
    # raw_type = sg.popup_get_text("Enter the RAW file type for your images")
    # destination = sg.popup_get_folder("Enter the name of the folder in which you would want to store these images")

    # try:
    #     file = open(filename)
    # except:
    #     sg.popup_error("Could not find the file list")

    # import_list(file, raw_type)
    # sort_folder(destination)
    
main()
