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
mx_recon.py takes a domain name, checks for an MX record, and if found checks for SPF and DMARC records, printing matches.  
I plan to add more functionality later.  
______________________________________________________________
**Some functionality ideas:  **
* check MX Hostnames against known mail providers (Google, Cisco, Outlook, AWS, etc)  
* check SPF hostnames against MX hostnames to gauge SPF health  
* check SPF final action to gauge SPF health  
* check DMARC percentage and final action to gauge DMARC health  
* save results to a file  
* read csv list of domains, output multiple results files
