""" version 0.1.5, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver
import re

domain = input("Enter a Domain to check: ")
#domain = "test.com"
outputfile = domain + ".txt"
with open(outputfile, "w") as opf:
    try:
        test_mx = dns.resolver.resolve(domain, "MX")
        print("########################################")
        print("# MX Records Found:\n# \tPriority\t|\tHostname\t|\tSuspected Service")
        #opf.write("########################################\n")
        #opf.write("# MX Records Found:\n# \tPriority\tHostname\n")
        for mx_data in test_mx:
            mx_results = str(mx_data)
            #opf.write("# \t" + mx_results + "\n")
            # parse out suspected email gateway
            rmx = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9_-]*["
                             r"a-zA-Z0-9])?", mx_results)
            rmxval = re.findall(r"\.[a-zA-Z0-9]*\.[comi]{2,3}", str(rmx))
            if rmxval == ['.iphmx.com']:
                print("# \t " + mx_results + "\tCisco Secure Email Host")
            elif rmxval == ['.mimecast.com']:
                print("# \t " + mx_results + "\tMimecast Cloud Email Security Host")
            elif rmxval == ['.zixmail.net']:
                print("# \t " + mx_results + "\tPossibly Zixmail Host")
            elif rmxval == ['.google.com']:
                print("# \t " + mx_results + "\tGoogle Workspaces Host")
            elif rmxval == ['.outlook.com']:
                print("# \t " + mx_results + "\tPossibly O365 Host")
            elif rmxval == ['.onmicrosoft.com']:
                print("# \t " + mx_results + "\tPossibly O365 Host")
            elif rmxval == ['.zoho.com']:
                print("# \t " + mx_results + "\tZoho Host")
            elif rmxval == ['.messagingengine.com']:
                print("# \t " + mx_results + "\tFastmail Host")
            elif rmxval == ['.amazonaws.com']:
                print("# \t " + mx_results + "\tAmazon WorkMail Host")
            elif rmxval == ['.emailsvr.com']:
                print("# \t " + mx_results + "\tRackspace Cloud Office Host")
            elif rmxval == ['.spamtitan.com']:
                print("# \t " + mx_results + "\tSpamTitan Cloud Email Security Host")
            elif rmxval == ['.onice.io']:
                print("# \t " + mx_results + "\tIceWarp Cloud Email Host")
            elif rmxval == ['.mxrecord.io']:
                print("# \t " + mx_results + "\tCloudflare Area 1 Email Security Host")
            elif rmxval == ['.messagelabs.com']:
                print("# \t " + mx_results + "\tSymantec Email Security.cloud Host")
            else:
                print("# \t" + mx_results + "\tUnrecognized Host")
    except:
        print("# [FAIL] MX Record Not Found.\n")
        #opf.write("# [FAIL] MX Record Not Found.\n")
        pass

    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        print("########################################")
        #opf.write("########################################\n")
        for spf_data in test_spf:
            spf_results = str(spf_data)
            if 'spf1' in str(spf_data):
                print("# SPF Record Found:\n#\t", spf_data)
                #opf.write("# SPF Record Found:\n#\t" + spf_results + "\n")
                print("# \tSPF Details:")
                # regex for redirects
                try:
                    rredir = re.findall(r"(?i)[redict]{8}=(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                        r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rredirval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                           r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rredir))
                    if rredir == []:
                        print("# \t\t...Not Declared: Redirect.")
                    else:
                        print("# \t\tRedirects to: " + str(rredirval))
                except: 
                    pass

                # regex for includes
                try:
                    rinc = re.findall(r"(?i)[include]{7}:(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rincval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                         r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rinc))
                    if rincval == []:
                        print("# \t\t...Not Declared: Includes.")
                    else:
                        print("# \t\tIncludes: " + str(rincval))
                except:
                    pass
                # regex for ipv4's??? COUNT???

                # regex for ipv6's??? COUNT???

                # regex for other macros??? UGH!!!
                try:
                    rmac = re.findall(r"[%{]{2}[a-zA-Z]{1}[}]{1}", spf_results)
                    if rmac == []:
                        print("# \t\t...Not Declared: Misc Macros.")
                    else:
                        print("# \t\tMisc Macros: " + str(rmac))
                except:
                    pass

                # regex for all action CHAIN OF IF ELSE ELSE ELSE
                try:
                    rall = re.findall(r"(?i)[?+~-]{1}all\"$", spf_results)
                    rallval = re.findall(r"[?+~-]{1}", str(rall))
                    if rallval == ['?']:
                        print("# \t\tAll Mechanism: " + str(rallval) + " NEUTRAL.")
                    elif rallval == ['+']:
                        print("# \t\tAll Mechanism: " + str(rallval) + " PASS.")
                    elif rallval == ['~']:
                        print("# \t\tAll Mechanism: " + str(rallval) + " SOFTFAIL.")
                    elif rallval == ['-']:
                        print("# \t\tAll Mechanism: " + str(rallval) + " HARDFAIL.")
                    else:
                        print("# \t\t...Not Declared: All Mechanism.")
                except:
                    pass

    except:
        print("# [FAIL] SPF Record Not Found.")
        #opf.write("# [FAIL] SPF Record Not Found.\n")
        pass

    try:
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        print("########################################")
        #opf.write("########################################\n")
        for dmarc_data in test_dmarc:
            dmarc_results = str(dmarc_data)
            if "DMARC1" in str(dmarc_data):
                print("# DMARC Record Found:\n#\t", dmarc_data)
                #opf.write("# DMARC Record Found:\n#\t" + dmarc_results + "\n")
                print("# \tDMARC Details:")
                # DMARC RUA Recipient
                try:
                    rrua = re.findall(r"[a-zA-Z][a-zA-Z][aA]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rruaval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rrua))
                    if rruaval == []:
                        print("# \t\t...Not Declared: Reports Aggregate Recipient (rua=<user@domain.com>).")
                    else:
                        print("# \t\tReports Aggregate Recipient: " + str(rruaval))
                except:
                    print("# \tReports Aggregate Recipient Not Declared.")
                # DMARC RUF Recipient
                try:
                    rruf = re.findall(r"[a-zA-Z][a-zA-Z][fF]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rrufval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rruf))
                    if rrufval == []:
                        print("# \t\t...Not Declared: Reports Forensic Recipient (ruf=<user@domain.com>).")
                    else:
                        print("# \t\tReports Forensic Recipient: " + str(rrufval))
                except:
                    print("# \tReports Forensic Recipient Not Declared.")
                # DMARC DKIM Alignment
                try:
                    radkim = re.findall(r"(?i)[adkim]{5}=[sr]{1};", dmarc_results)
                    radkimval = re.findall(r"[sS,rR]", str(radkim))
                    if radkimval == []:
                        print("# \t\t...Not Declared: DKIM Alignment (adkim=<s|r>).")
                    else:
                        print("# \t\tDKIM Alignment Strict/Relaxed: " + str(radkimval))
                except:
                    print("# \tDKIM Alignment Not Declared.")
                # DMARC SPF Alignment
                try:
                    raspf = re.findall(r"(?i)[aspf]{4}=[sr]{1};", dmarc_results)
                    raspfval = re.findall(r"[sS,rR]", str(raspf))
                    if raspfval == []:
                        print("# \t\t...Not Declared: SPF Alignment (aspf=<s|r>).")
                    else:
                        print("# \t\tSPF Alignment Strict/Relaxed: " + str(raspfval))
                except:
                    print("# \tSPF Alignment Not Declared.")
                # DMARC Percentage Filtered
                try:
                    rpct = re.findall(r"(?i)[pct]{3}=[0-9]{2,3}", dmarc_results)
                    rpctval = re.findall(r"[0-9]{2,3}", str(rpct))
                    if rpctval == []:
                        print("# \t\t...Not Declared: Percentage Msgs Filtered (pct=<0-100>).")
                    else:
                        print("# \t\tPercentage Msgs Filtered: " + str(rpctval))
                except:
                    print("# \tPercentage Msgs Filtered Not Declared.")
                # DMARC Subdomain Policy Action
                try:
                    rsp = re.findall(r"(?i)[sp]{2}=[a-zA-Z]*;", dmarc_results)
                    rspval = re.findall(r"[a-zA-Z]{4,10}", str(rsp))
                    if rspval == []:
                        print("# \t\t...Not Declared: Subdomain Policy Action (sp=<none|reject|quarantine>).")
                    else:
                        print("# \t\tSubdomain Policy Action: " + str(rspval))
                except:
                    print(" \tSubdomain Policy Action Not Declared.")
                # DMARC Policy Action
                try:
                    rp = re.findall(r"(?i)[p]{1}=[a-zA-Z]*;", dmarc_results)
                    rpval = re.findall(r"[a-zA-Z]{4,10}", str(rp))
                    if rpval == []:
                        print("# \t\t...Uh Oh! Not Declared: Policy Action (p=<none|reject|quarantine>).")
                    else:
                        print("# \t\tPolicy Action: " + str(rpval))
                except:
                    print(" \tPolicy Action Not Declared.")

    except:
        print("# [FAIL] DMARC Record Not Found.")
        #opf.write("# [FAIL] DMARC Record Not Found.\n")
        pass

opf.close()
#input("\nPress enter to exit ")
