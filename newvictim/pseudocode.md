Banner, because banners are cool!  
Name, date, version  

check for root  
if not root, disclaimer text, exit  

Ask for input: What is the new lab's name?  
Input = LabMachineName  
Ask for input: What is the new lab's IP address?  
Input = RHOST  

os.system touch ./LabMachineName  
os.system cp ./CTF_NOTES.ctb ./LabMachineName/LabMachineName_Recon.ctb  
os.system cp ./GenericRecon.py ./LabMachineName/  
os.system touch ./LabMachineName/notes.txt  
os.system touch ./LabMachineName/Payloads/  

os.system ping RHOST -t 5  
if success  
  cherrytree LabMachineName_Recon.ctb &  
  GenericRecon.py RHOST  
