Banner, because banners are cool!  
Name, date, version  

check for root  
if not root, disclaimer text, exit  

Ask for input: What is the new lab's name?  
Input = LabMachineName  
Ask for input: What is the new lab's IP address?  
Input = RHOST  

os.system touch ./LabMachineName  
if CTF_NOTES.ctb exists,  
  os.system cp ./CTF_NOTES.ctb ./LabMachineName/LabMachineName_Recon.ctb  
  else wget from github/cpardue/resources  
  os.system cp ./CTF_NOTES.ctb ./LabMachineName/LabMachineName_Recon.ctb  
if GenericRecon.py exists,  
  os.system cp ./GenericRecon.py ./LabMachineName/  
  else wget from github/cpardue/resources  
  os.system cp ./GenericRecon.py ./LabMachineName/  
os.system touch ./LabMachineName/notes.txt  
os.system touch ./LabMachineName/Payloads/  

os.system ping RHOST -t 5  
if success  
  os.system open cherrytree LabMachineName_Recon.ctb &  

Ask for input: Do you want to run GenericRecon.py? y/n
Input = GenericReconAnswer
if GenericReconAnswer, 
  os.system run GenericRecon.py RHOST  
  else exit
