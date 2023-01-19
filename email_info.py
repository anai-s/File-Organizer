import os

header = {}
header['fromaddr'] = "from@gmail.com"
header['fromname'] = "File Organizer"
header['fromapppwd'] = "xxxxxxxxxxxxx" # Gmail application password
header['toaddr'] = "to@hotmail.fr"
header['toname'] = "Anais" # Only change if you don't want the username of your machine session
header['subject'] = "[Reminder] It's time to organize your files"
smtp = 'smtp.gmail.com'
intro = f"Hello {header['toname']},\n\nThis is a kind reminder to organize your files. Here is the list of all the files to sort:\n\n"
def content():
    files_list = ""
    for directory, subdir_list, file_list in os.walk("C:\\Users\\anais\\Documents\\To sort"):
        if len(file_list):
            files_list += 'Directory: %s \n'%(directory)
        for name in file_list:
            files_list += 'File: %s \n' %(name)

    return intro + files_list
