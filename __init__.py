import os
import shutil
#import email_info as email_info
#from send_email import SendEmail
from format import File

os.chdir("C:\\Users\\anais\\Downloads")

# The loop will run into Downloads folder and move the files into the subfolders of the directory


for file in os.listdir():
    i = 1
    dest = None
    f = File(file)
    dest = f.file_destination() # indicate the directory where the file should be moved
    if dest != None:
        renamed_file = file
        while os.path.exists(os.path.join(dest,renamed_file)): # file is renamed if it already exists in dest 
            renamed_file = os.path.splitext(file)[0] + " (" + str(i) + ")" + os.path.splitext(file)[1]
            i += 1
        if renamed_file != file:
            os.rename(file,renamed_file)
        if not os.path.exists(dest): # directory dest is created if it doesn't already exist
            os.makedirs(dest)
        shutil.move(renamed_file, dest) # move file to new directory

"""
# Send a kind reminder to my email address to clean my directory C:\\Users\\anais\\Documents\\A Trier


s = SendEmail()
s.set_up(params=email_info.header)
s.send_email(content=email_info.content())

"""