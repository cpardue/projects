### MX Recon

**TL;DR**  
I often do an nslookup and check MXToolbox for some info.  
So why not make a python script amiright  
______________________________________________________________
**Prereq's**  
Python3  
dnspython python package (pip install dnspython)
______________________________________________________________
**Details**  
Run it, enter a domain into the prompt, see a check. 
mx_recon.py takes a domain name, checks for an MX record, and if found checks for SPF and DMARC records, printing matches.  
I plan to add more functionality later.  
Just wrote this up on a day off so that I have a skeleton to work with.  
______________________________________________________________
**Some functionality ideas:**  
* check MX Hostnames against known mail providers (Google, Cisco, Outlook, AWS, etc)  
* check SPF hostnames against MX hostnames to gauge SPF health  
* check SPF final action to gauge SPF health  
* check DMARC percentage and final action to gauge DMARC health  
* save results to a file  
* read csv list of domains, output multiple results files

<p align=center>
<a href="https://www.buymeacoffee.com/cpardue0" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
