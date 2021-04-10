################################################
####### Written by Chris Pardue in 2021 ########
########## https://cpardue.github.io ###########
############## Written in Python3 ##############
################################################
# !#/bin/python3 # wrong path, not universal for others

import os
import sys
import subprocess



os.system("clear") # clear the terminal
print("#########################################################")
print("#     ______ ______ _   __ ______ ____   ____ ______    #")
print("#    / ____// ____// | / // ____// __ \ /  _// ____/    #")
print("#   / / __ / __/  /  |/ // __/  / /_/ / / / / /         #")
print("#  / /_/ // /___ / /|  // /___ / _, _/_/ / / /___       #")
print("#  \____//_____//_/ |_//_____//_/_|_|/___/_\____/____   #")
print("#    / ___/ / ____//   |   / | / // | / // ____// __ \  #")
print("#    \__ \ / /    / /| |  /  |/ //  |/ // __/  / /_/ /  #")
print("#   ___/ // /___ / ___ | / /|  // /|  // /___ / _, _/   #")
print("#  /____/ \____//_/  |_|/_/ |_//_/ |_//_____//_/ |_|    #")
print("# by cpardue circa 2021     ver1.0    cpardue.github.io #")
print("#########################################################")
print(" from github.com/cpardue/projects/tree/main/GenericRecon ")
print("\n")
if not os.geteuid()==0: # check for root
    sys.exit('This script must be run as root!')
print("We'll need to dump scans into a folder...")
folder_name = input("Create a new folder name :") # ask user for input_folder_name
print(folder_name)
print("We'll need a target hostname or IP to scan...")
target_IP = input("Enter target hostname or IP : ") # ask user for input_target_IP
print(target_IP)
os.system("mkdir " + folder_name) # mkdir ./folder_name
print("...Created folder " + folder_name + " to hold scan results.")

os.system("touch ./" + folder_name + "/1_nmap_sweep.txt") # initalizing textfile, maybe not necessary
print("...Created 1_nmap_sweep.txt within " + folder_name)
print("Starting initial nmap scan and dumping into 1_nmap_sweep.txt...")
nmap_sweep = os.system("nmap -Pn -p- -T5 -oN ./" + folder_name + "/1_nmap_sweep.txt " + target_IP) # nmap all port sweep
print(nmap_sweep) # output it to the terminal
print("...DONE!\n")
print("Processing open ports into open_ports.txt...")
get_ports_open = os.system("cat " + folder_name + "/1_nmap_sweep.txt | grep ^[:0-9:] | grep open | awk '{print $1}' | sed 's/\/tcp//g' > ./ports_open.txt") # filter scan by lines staring with #'s, then "open", then print first column, then remove "/tcp", place in new file
print(get_ports_open)
print("...DONE!\n")
print("Processing open http ports into ports_http.txt...")
get_ports_http = os.system("cat " + folder_name + "/1_nmap_sweep.txt | grep ^[:0-9:] | grep http | awk '{print $1}' | sed 's/\/tcp//g' > ./ports_http.txt") # do same as above but with "http" instead of "open"
print(get_ports_http)
print("...DONE!\n")

os.system("touch ./" + folder_name + "/2_nmap_scan.txt") # initializing textfile, maybe not necessary
print("...Created file 2_nmap_scan.txt within " + folder_name)
print("Starting second nmap scan and dumping into 2_nmap_scan...")
nmap_scan = os.system("nmap -Pn -A --script=vuln -p $(tr '\n' , <./ports_open.txt) -oN ./" + folder_name + "/2_nmap_scan.txt " + target_IP) # run aggressive and NSE vulnerability scan against only the open ports
print(nmap_scan) # print out the ongoing scan
print("...DONE!\n") # when above is done, print done and move on

ports_http = open("ports_http.txt","r") # open ports_http.txt and read it
for line in ports_http: # for each http port in file...
    line_without_breaks = line.replace("\n", "") # remove line breaks which are messing up gobuster_scan
    print("Starting gobuster...")
    gobuster_scan1 = 'gobuster dir -e -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -u http://' # breaking up system commands with variables
    gobuster_scan2 = ':'
    gobuster_scan3 = ' > output.txt' # we're saving the output as output.txt
    gobuster_scan = os.system(gobuster_scan1 + target_IP + gobuster_scan2 + line_without_breaks + gobuster_scan3) # reassembling commands and variables as string
    print("moving output.txt to 3_gobuster_" + line_without_breaks + ".txt")
    os.system("mv ./output.txt " + folder_name + "/3_gobuster_scan_" + line_without_breaks + ".txt") # move/rename output.txt to folder_name
    print("Done with loop of " + line_without_breaks)
ports_http.close() # close ports_http.txt reading when last line is iterated through

ports_http = open("ports_http.txt","r") # open ports_http.txt and read it
for line in ports_http: # for each http port in file...
    line_without_breaks = line.replace("\n", "") # remove line breaks which are messing up gobuster_scan
    print("Starting wfuzz...")
    wfuzz_scan1 = 'wfuzz -c --sc 200,201,202,203,204,205,206 -f suboutput.txt -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H Host:FUZZ.'# breaking up system commands with variables
    wfuzz_scan2 = ':' # will use this one twice
    wfuzz_scan3 = ' -u http://'
    wfuzz_scan4 = ' > output.txt' # we're saving the output as output.txt
    wfuzz_scan = os.system(wfuzz_scan1 + target_IP + wfuzz_scan2 + line_without_breaks + wfuzz_scan3 + target_IP + wfuzz_scan2 + line_without_breaks) # reassembling commands and variables as string
    print("moving suboutput.txt to 3_wfuzz_" + line_without_breaks + ".txt")
    os.system("mv ./suboutput.txt " + folder_name + "/3_wfuzz_scan_" + line_without_breaks + ".txt") # move/rename output.txt to folder_name
    print("Done with loop of " + line_without_breaks)
ports_http.close() # close ports_http.txt reading when last line is iterated through

print("Cleaning up files...") # clean up the root folder ports_open.txt and ports_http.txt
cleanup = os.system("rm -rf ports_*.txt")
print(cleanup)
print("...DONE!\n")
