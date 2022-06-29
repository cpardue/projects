newvictim.py  

Prereq's  
1. For use with Hackthebox lab machines  
2. Run from Chris' attack machine  
3. Victim is fresh, has no prev documentation||folders on attack machine  

Purpose  
Once a new htb lab machine has been selected, run this script to perform the following:  
* Create a fresh Folder named LabMachineName  
* Copy a fresh CherryTree Recon template to the Folder named LabMachineName  
* Rename the fresh template to LabMachineName_Recon  
* Copy a fresh GenericRecon.py script to the Folder named LabMachineName (so you can modify if neded/re-run)  
* Create a new notes.txt in the Folder  
* Create a ./Payloads Subfolder
* Ping the lab machine  
* If lab machine is up, open LabMachineName_Recon && run GenericRecon.py against the machine

This should give you a good head start on a new machine, more importantly it will KEEP YOUR STUFF ORGANIZED!
