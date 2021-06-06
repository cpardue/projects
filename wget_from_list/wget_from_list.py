import os
import sys
import subprocess

os.system("clear")  # clear the terminal
URL_list = input("Name of URL list to iteratively wget? :")  # ask for URL_list
URL_list_read = open(URL_list,"r")  # open URL_list and read it
for URL in URL_list_read:  # for URL in URL_list
    os.system("wget " + URL)  # wget URL
    print("wget wGOT!")
URL_list_read.close()
print("Most likely done.  Check your parent directory to see.")
