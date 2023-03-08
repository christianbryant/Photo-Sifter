# Photo-Sifter
## Explanation
While taking many photos with my Sony A7iii, I run into the issue of having to go through the lower .jpgs to find each photo I want to edit, then having to search through the folder again to find the respective raw. So I created this to shift through my images folder on my SD card to create a folder and add the files I want to edit.

## Installation
Tested on Windows 10 and macOS Ventura 13.0.1\
Please make sure you have Python3 installed on your system to use this file and have updated it to the most current version (Python 3.10.10).\
Place the main.py into the folder that has all of your photo RAWS.\
Once installed you can move on to usage.

## Usage
### Windows 10
In the folder where the images are, shift+right-click in an empty spot and select "Open Powershell Window Here" and paste the following command:
```bash
python3 main.py DESTINATION_FOLDER_NAME FILE_LIST.txt RAW_TYPE
```
If you recieve an error idicating no python is found, please install the python version 3.10 via the Windows Microsoft Store if on Windows\
### macOS
On your Mac, open a Finder window, then navigate to the folder you want to use.\
If you don’t see the path bar at the bottom of the Finder window, choose View > Show Path Bar.\
Control-click the folder in the path bar, then do one of the following.\
Open a new window: Choose Open in Terminal.\
Provided by: https://support.apple.com/guide/terminal/open-new-terminal-windows-and-tabs-trmlb20c7888/mac#:~:text=Open%20new%20Terminal%20windows%20or%20tabs%20from%20the%20Finder&text=Control-click%20the%20folder%20in,New%20Terminal%20Tab%20at%20Folder. \
If you recieve an error idicating no python is found, make sure you have Homebrew installed on your system, then write the following command:
```base
brew install python
```
### Usage not dependent on operating system
Be sure NOT to include the file type in the .txt.\
Example .txt file for reference:
```txt
_DSC3041
_DSC3127
_DSC3198
_DSC3236
_DSC3251
_DSC3263
_DSC3275
_DSC3278
_DSC3279
_DSC3281
_DSC3284
_DSC3348
_DSC3406
_DSC3503
_DSC3517
_DSC3523
_DSC3574
```
The program shall print the following example information if successful:
If the Folder hasn't been created before usage:
```bash
Found 17 file names in file provided
Folder created at J:\DCIM\100MSDCF\need_to_edit
Moved file _DSC3041.ARW
Moved file _DSC3127.ARW
Moved file _DSC3198.ARW
Moved file _DSC3236.ARW
Moved file _DSC3251.ARW
Moved file _DSC3263.ARW
Moved file _DSC3275.ARW
Moved file _DSC3278.ARW
Moved file _DSC3279.ARW
Moved file _DSC3281.ARW
Moved file _DSC3284.ARW
Moved file _DSC3348.ARW
Moved file _DSC3406.ARW
Moved file _DSC3503.ARW
Moved file _DSC3517.ARW
Moved file _DSC3523.ARW
Moved file _DSC3574.ARW
Moved 17 files to folder J:\DCIM\100MSDCF\need_to_edit
```
If Folder has been created before usage:
```bash
Found 17 file names in file provided
Folder moved to J:\DCIM\100MSDCF\need_to_edit
Moved file _DSC3041.ARW
Moved file _DSC3127.ARW
Moved file _DSC3198.ARW
Moved file _DSC3236.ARW
Moved file _DSC3251.ARW
Moved file _DSC3263.ARW
Moved file _DSC3275.ARW
Moved file _DSC3278.ARW
Moved file _DSC3279.ARW
Moved file _DSC3281.ARW
Moved file _DSC3284.ARW
Moved file _DSC3348.ARW
Moved file _DSC3406.ARW
Moved file _DSC3503.ARW
Moved file _DSC3517.ARW
Moved file _DSC3523.ARW
Moved file _DSC3574.ARW
Moved 17 files to folder J:\DCIM\100MSDCF\need_to_edit
```

## Errors
If this error is caught, it means you did not provide the correct amount of command line arguments while running the script:
```bash
Exception: Please provide command line input as follows:
 python3 main.py DESTINATION_FOLDER_NAME FILE_LIST.txt RAW_TYPE
 ```
 If this error is caught, it means there was nothing in the text file provided:
 ```bash
 Exception: No lines in provided file!
 ```
 If this error is caught, it means there is no text file in the same directory as the python script:
 ```bash
 Exception: Could not find the file list
 ```
 If this error is caught, it means there is no image files in the same directory that the python script is in (If file count is less than 3 in the directory):
 ```bash
 Exception: No image files present!
 ```
 If this error is caught, then there were no files in the directory that had the same name as any of the names of the files provided in the .txt file:
 ```bash
 Exception: Found none of the files that were provided in the file list!
