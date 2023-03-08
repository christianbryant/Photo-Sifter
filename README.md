# Photo-Sifter
## Installation

Please make sure you have Python3 installed on your system to use this file and have updated it to the most current version (Python 3.10.10).
Place the main.py into the folder that has all of your photo RAWS.
Once installed you can move onto usage.

## Usage
```bash
python3 main.py DESTINATION_FOLDER_NAME FILE_LIST.txt RAW_TYPE
```
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
If Folder hasnt been created before usage:
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
 Exception: No lines in provide file!
 ```
 If this error is caught, it means there is no text file in the same directory as the python script:
 ```bash
 Exception: Could not find the file list
 ```
 If this error is caught, it means there is no image files in the same directory that the python script is in (If file count is less than 3 in the directory):
 ```bash
 Exception: No image files present!
 ```
 If this error is caught, then there were no files in the directory that had the same name as the any of the files names provided in the .txt file:
 ```bash
 Exception: Found none of the files that were provided in the file list!
