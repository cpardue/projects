""" version 0.1.6, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver
import re

domain = input("Enter a Domain to check: ")
#domain = "test.com"
# name the output file
outputfile = domain + ".txt"
# create & open the output file and...
with open(outputfile, "w") as opf:
    # try looking for MX records
    try:
        test_mx = dns.resolver.resolve(domain, "MX")
        opf.write("###########################################################################################\n")
        opf.write("# MX Records Found:\n# \tPriority\t|\tHostname\t|\tSuspected Service\n")
        # look inside results, loop through w/regex to parse it out
        for mx_data in test_mx:
            mx_results = str(mx_data)
            # parse out suspected email gateway
            rmx = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9_-]*["
                             r"a-zA-Z0-9])?", mx_results)
            rmxval = re.findall(r"\.[a-zA-Z0-9]*\.[comi]{2,3}", str(rmx))
            if rmxval == ['.iphmx.com']:
                opf.write("# \t " + mx_results + "\tCisco Secure Email Host\n")
            elif rmxval == ['.mimecast.com']:
                opf.write("# \t " + mx_results + "\tMimecast Cloud Email Security Host\n")
            elif rmxval == ['.zixmail.net']:
                opf.write("# \t " + mx_results + "\tPossibly Zixmail Host\n")
            elif rmxval == ['.google.com']:
                opf.write("# \t " + mx_results + "\tGoogle Workspaces Host\n")
            elif rmxval == ['.outlook.com']:
                opf.write("# \t " + mx_results + "\tPossibly O365 Host\n")
            elif rmxval == ['.onmicrosoft.com']:
                opf.write("# \t " + mx_results + "\tPossibly O365 Host\n")
            elif rmxval == ['.zoho.com']:
                opf.write("# \t " + mx_results + "\tZoho Host\n")
            elif rmxval == ['.messagingengine.com']:
                opf.write("# \t " + mx_results + "\tFastmail Host\n")
            elif rmxval == ['.amazonaws.com']:
                opf.write("# \t " + mx_results + "\tAmazon WorkMail Host\n")
            elif rmxval == ['.emailsvr.com']:
                opf.write("# \t " + mx_results + "\tRackspace Cloud Office Host\n")
            elif rmxval == ['.spamtitan.com']:
                opf.write("# \t " + mx_results + "\tSpamTitan Cloud Email Security Host\n")
            elif rmxval == ['.onice.io']:
                opf.write("# \t " + mx_results + "\tIceWarp Cloud Email Host\n")
            elif rmxval == ['.mxrecord.io']:
                opf.write("# \t " + mx_results + "\tCloudflare Area 1 Email Security Host\n")
            elif rmxval == ['.messagelabs.com']:
                opf.write("# \t " + mx_results + "\tSymantec Email Security.cloud Host\n")
            else:
                opf.write("# \t" + mx_results + "\tUnrecognized Host\n")
    # if mx records not found...
    except:
        opf.write("# [FAIL] MX Record Not Found.\n#\n")
        pass
    # try looking for spf record
    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        opf.write("###########################################################################################\n")
        # look inside results, loop through w/regex to parse it out
        for spf_data in test_spf:
            spf_results = str(spf_data)
            if 'spf1' in str(spf_data):
                opf.write("# SPF Record Found:\n#\t" + spf_results + "\n#\n")
                opf.write("# \tSPF Details:\n")
                # regex for redirects
                try:
                    rredir = re.findall(r"(?i)[redict]{8}=(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                        r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rredirval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                           r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rredir))
                    if rredir == []:
                        opf.write("# \t\t...Not Declared: Redirect.\n")
                    else:
                        opf.write("# \t\tRedirects to: " + str(rredirval) + "\n")
                except: 
                    pass

                # regex for includes
                try:
                    rinc = re.findall(r"(?i)[include]{7}:(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rincval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                         r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rinc))
                    if rincval == []:
                        opf.write("# \t\t...Not Declared: Includes.\n")
                    else:
                        opf.write("# \t\tIncludes: " + str(rincval) + "\n")
                except:
                    pass
                # regex for ipv4's??? COUNT???

                # regex for ipv6's??? COUNT???

                # regex for other macros??? UGH!!!
                try:
                    rmac = re.findall(r"[%{]{2}[a-zA-Z][}]", spf_results)
                    if rmac == []:
                        opf.write("# \t\t...Not Declared: Misc Macros.\n")
                    else:
                        opf.write("# \t\tMisc Macros: " + str(rmac) + "\n")
                except:
                    pass

                # regex for all action CHAIN OF IF ELSE ELSE ELSE
                try:
                    rall = re.findall(r"(?i)[?+~-]all\"$", spf_results)
                    rallval = re.findall(r"[?+~-]", str(rall))
                    if rallval == ['?']:
                        opf.write("# \t\tAll Mechanism: " + str(rallval) + " NEUTRAL.\n")
                    elif rallval == ['+']:
                        opf.write("# \t\tAll Mechanism: " + str(rallval) + " PASS.\n")
                    elif rallval == ['~']:
                        opf.write("# \t\tAll Mechanism: " + str(rallval) + " SOFTFAIL.\n")
                    elif rallval == ['-']:
                        opf.write("# \t\tAll Mechanism: " + str(rallval) + " HARDFAIL.\n")
                    else:
                        opf.write("# \t\t...Not Declared: All Mechanism.\n")
                except:
                    pass
    # if no spf record found...
    except:
        opf.write("# [FAIL] SPF Record Not Found.\n#\n")
        pass
    # try looking for dmarc record
    try:
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        opf.write("###########################################################################################\n")
        # look inside results, loop through w/regex to parse it out
        for dmarc_data in test_dmarc:
            dmarc_results = str(dmarc_data)
            if "DMARC1" in str(dmarc_data):
                opf.write("# DMARC Record Found:\n#\t" + dmarc_results + "\n#\n")
                opf.write("# \tDMARC Details:\n")
                # DMARC RUA Recipient
                try:
                    rrua = re.findall(r"[a-zA-Z][a-zA-Z][aA]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rruaval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rrua))
                    if rruaval == []:
                        opf.write("# \t\t...Not Declared: Reports Aggregate Recipient (rua=<user@domain.com>).\n")
                    else:
                        opf.write("# \t\tReports Aggregate Recipient: " + str(rruaval) + "\n")
                except:
                    opf.write("# \tReports Aggregate Recipient Not Declared.\n")
                # DMARC RUF Recipient
                try:
                    rruf = re.findall(r"[a-zA-Z][a-zA-Z][fF]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rrufval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rruf))
                    if rrufval == []:
                        opf.write("# \t\t...Not Declared: Reports Forensic Recipient (ruf=<user@domain.com>).\n")
                    else:
                        opf.write("# \t\tReports Forensic Recipient: " + str(rrufval) + "\n")
                except:
                    opf.write("# \tReports Forensic Recipient Not Declared.\n")
                # DMARC DKIM Alignment
                try:
                    radkim = re.findall(r"(?i)[adkim]{5}=[sr];", dmarc_results)
                    radkimval = re.findall(r"[sS,rR]", str(radkim))
                    if radkimval == []:
                        opf.write("# \t\t...Not Declared: DKIM Alignment (adkim=<s|r>).\n")
                    else:
                        opf.write("# \t\tDKIM Alignment Strict/Relaxed: " + str(radkimval) + "\n")
                except:
                    opf.write("# \tDKIM Alignment Not Declared.\n")
                # DMARC SPF Alignment
                try:
                    raspf = re.findall(r"(?i)[aspf]{4}=[sr];", dmarc_results)
                    raspfval = re.findall(r"[sS,rR]", str(raspf))
                    if raspfval == []:
                        opf.write("# \t\t...Not Declared: SPF Alignment (aspf=<s|r>).\n")
                    else:
                        opf.write("# \t\tSPF Alignment Strict/Relaxed: " + str(raspfval) + "\n")
                except:
                    opf.write("# \tSPF Alignment Not Declared.\n")
                # DMARC Percentage Filtered
                try:
                    rpct = re.findall(r"(?i)[pct]{3}=[0-9]{2,3}", dmarc_results)
                    rpctval = re.findall(r"[0-9]{2,3}", str(rpct))
                    if rpctval == []:
                        opf.write("# \t\t...Not Declared: Percentage Msgs Filtered (pct=<0-100>).\n")
                    else:
                        opf.write("# \t\tPercentage Msgs Filtered: " + str(rpctval) + "\n")
                except:
                    opf.write("# \tPercentage Msgs Filtered Not Declared.\n")
                # DMARC Subdomain Policy Action
                try:
                    rsp = re.findall(r"(?i)[sp]{2}=[a-zA-Z]*;", dmarc_results)
                    rspval = re.findall(r"[a-zA-Z]{4,10}", str(rsp))
                    if rspval == []:
                        opf.write("# \t\t...Not Declared: Subdomain Policy Action (sp=<none|reject|quarantine>).\n")
                    else:
                        opf.write("# \t\tSubdomain Policy Action: " + str(rspval) + "\n")
                except:
                    opf.write(" \tSubdomain Policy Action Not Declared.\n")
                # DMARC Policy Action
                try:
                    rp = re.findall(r"(?i)[p]=[a-zA-Z]*;", dmarc_results)
                    rpval = re.findall(r"[a-zA-Z]{4,10}", str(rp))
                    if rpval == []:
                        opf.write("# \t\t...Uh Oh! Not Declared: Policy Action (p=<none|reject|quarantine>).\n")
                    else:
                        opf.write("# \t\tPolicy Action: " + str(rpval) + "\n")
                except:
                    opf.write(" \tPolicy Action Not Declared.\n")
    # if no dmarc record found...
    except:
        opf.write("# [FAIL] DMARC Record Not Found.\n#\n")
        pass

opf.close()
#input("\nPress enter to exit ")
