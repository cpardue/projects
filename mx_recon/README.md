### MX Recon

**TL;DR**  
I often do an nslookup and check MXToolbox for some info.  
So why not make a python script amiright  
______________________________________________________________  

**instructions**  

initial setup:  
1. download the files.  
2. change directory to download location.
3. run 'pip install -r requirements.txt' to install dependencies. 

usage:  
6. run the script  
7. enter a domain name (example.com) at the prompt
8. press any key to exit
9. your example.com.txt report is now ready in the script's folder  
______________________________________________________________  

**Progress Report**  
Currently accepts input for a domain name, runs MX, SPF, DMARC checks and writes to a file named <domain>.txt, including minor details such as hardfail, softfail, p=none, etc. Working on finishing it so I can move on with clear conscience.<br>
  Added file output to domain.com.txt.<br>
  Added a mini digest of cloud email gateway hosts for mx host identification.<br>
  Added SPF details parsing.<br>
  Added logging for info and debug.<br>
Give it a try. If you like it, steal it and make it your own. 
______________________________________________________________  
  
**Some functionality ideas:**  
* check SPF final action to gauge SPF health - DONE  
* check DMARC percentage and policy action to gauge DMARC health - DONE 
* check MX Hostnames against known mail providers (Google, Cisco, Outlook, Proofpoint, etc) - DONE  
* save results to a file - DONE  
* check SPF hostnames against MX hostnames to gauge SPF health - Abandoned  
* logging enabled for troubleshooting - DONE
* argparse for accepting cli arguments - Pending  
* read csv list of domains, output multiple results files - Pending  




<p align=center>
<a href="https://www.buymeacoffee.com/cpardue0" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
