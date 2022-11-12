I made a thing and it works.  
  
Prerequisites:  
Assumes that it's run in kali  
Requires seclists installed at /usr/share (sudo apt-get install seclists -y)  
Requires python3  
  
Usage:  
$sudo python3 genericrecon.py  
  
Description:  
It's a single host recon script to scan for all open ports, then do an intensive scan of each open port, then do a gobuster scan of all open http ports, then do a wfuzz subdirectory scan of all open http ports, looking for 201, 202, 203, 204, 205, 206 response codes.  
When you start it, it will create a folder in it's directory with a name of your choosing, then ask for a target IP.  
Run it as root, modify it to suite your needs.  
  
May add more functionality to it later. 

<p align=center>
<a href="https://www.buymeacoffee.com/cpardue0" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
