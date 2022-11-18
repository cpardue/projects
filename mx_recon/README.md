### MX Recon

**TL;DR**  
I often do an nslookup and check MXToolbox for some info.  
So why not make a python script amiright  
______________________________________________________________
**Prereq's**  
Python3  
dnspython python package (pip install dnspython)
______________________________________________________________
**Progress Report**  
Currently accepts input for a domain name, runs MX, SPF, DMARC checks and writes to a file named <domain>.txt, including minor details such as hardfail, softfail, p=none, etc. Still working on functionality while bored. Works right now, although it needs cleanup of now-useless print statements. 
Give it a try. If you like it, steal it and make it your own. 
______________________________________________________________
**Some functionality ideas:**  
* check SPF final action to gauge SPF health - DONE  
* save results to a file - DONE  
* check DMARC percentage and policy action to gauge DMARC health - In Progress  
* check MX Hostnames against known mail providers (Google, Cisco, Outlook, Proofpoint, etc) - Pending  
* check SPF hostnames against MX hostnames to gauge SPF health - Pending  
* read csv list of domains, output multiple results files - Pending  
* argparse for accepting cli arguments - Pending  



<p align=center>
<a href="https://www.buymeacoffee.com/cpardue0" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
