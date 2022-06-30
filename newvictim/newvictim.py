################################################
####### Written by Chris Pardue in 2022 ########
########## https://chris-pardue.com ############
############## Written in Python3 ##############
################################################

import os
import sys
import subprocess



os.system("clear") # clear the terminal
print("##########################################################")
print("# by cpardue circa 2022         //         ___           #")
print("# github.com/cpardue/resources // |\ |    |__     |  |   #")
print("# chris-pardue.com            //  | \|    |___    |/\|   #")
print("# run from Boxes folder      //                          #")
print("# eat your wheaties         //         __  ___           #")
print("# wash your hands          //  \  / | /  `  |  |  |\/|   #")
print("#_________________________//    \/  | \__,  |  |  |  |   #")
print("#_________________________/                              #")
print("##########################################################")
print("\n")
if not os.geteuid()==0: # check for root
    sys.exit('This script must be run as root!')  #if not root, disclaimer text, exit
LabMachineName = input("What is the new lab's name :")  #Ask for input: What is the new lab's name? Input = LabMachineName
RHOST = input("What is the new lab's IP address :")  #Ask for input: What is the new lab's IP address? Input = RHOST

os.system("mkdir ./"+LabMachineName+"/")  #os.system touch ./LabMachineName
#if CTF_NOTES.ctb exists,
os.system("cp ./CTF_NOTES.ctb ./"+LabMachineName+"/"+LabMachineName+"_Recon.ctb")  #os.system cp ./CTF_NOTES.ctb ./LabMachineName/LabMachineName_Recon.ctb
#else wget from github/cpardue/resources
os.system("cp ./CTF_NOTES.ctb ./"+LabMachineName+"/"+LabMachineName+"_Recon.ctb")  #os.system cp ./CTF_NOTES.ctb ./LabMachineName/LabMachineName_Recon.ctb
#if GenericRecon.py exists,
os.system("cp ./GenericRecon.py ./"+LabMachineName+"/")  #os.system cp ./GenericRecon.py ./LabMachineName/
#else wget from github/cpardue/resources
os.system("cp ./GenericRecon.py ./"+LabMachineName+"/")  #os.system cp ./GenericRecon.py ./LabMachineName/
os.system("touch ./"+LabMachineName+"/Notes.txt")  #os.system touch ./LabMachineName/notes.txt
os.system("mkdir ./"+LabMachineName+"/Payloads/")  #os.system touch ./LabMachineName/Payloads/

print("Pinging host 5 times, if it's up then we'll open cherrytree and start GenericRecon...")  
os.system("ping "+RHOST+" -t 5")  #os.system ping RHOST -t 5
#if success
#need subprocess???
os.system("python2 cherrytree ./"+LabMachineName+"/"+LabMachineName"_Recon.ctb &")  #os.system open cherrytree LabMachineName_Recon.ctb &

#Ask for input: Do you want to run GenericRecon.py? y/n 
#Input = GenericReconAnswer 
#if GenericReconAnswer, 
#os.system run GenericRecon.py RHOST
#else exit
