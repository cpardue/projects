""" version 0.1.7, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver
import re
import logging

# logging setup
logging.basicConfig(level=logging.DEBUG)
# logging.debug('a debug log')
# logging.info('an info log')
# logging.warning('a warning log')
# logging.error('an error log')

version = "v0.1.7"

logging.debug("waiting on user input for domain to check...")
domain = input("Enter a Domain to check: ")
logging.debug("user gave input...")
# domain = "test.com"
logging.info("domain = " + domain)
# name the output file
outputfile = domain + ".txt"
logging.info("filename = " + outputfile)
# create & open the output file and...
with open(outputfile, "w") as opf:
    logging.debug("opened " + outputfile + " to write to...")
    # try looking for MX records
    try:
        logging.debug("trying to resolve MX records for " + domain + "...")
        test_mx = dns.resolver.resolve(domain, "MX")
        logging.debug(test_mx)
        opf.write("\t#################################\n")
        opf.write("\t#     mx_recon.py " + version + "        #\n")
        opf.write("\t#    written by Chris Pardue    #\n")
        opf.write("\t#   github.com/cpardue/python3  #\n")
        opf.write("\t#        buy me a coffee        #\n")
        opf.write("\t#################################\n\n")
        opf.write("MX Records Found:\n\t(Priority, Hostname, Suspected Service)\n")
        # look inside results, loop through w/regex to parse it out
        for mx_data in test_mx:
            logging.debug("checking MX record results for details...")
            mx_results = str(mx_data)
            logging.info(str(mx_data))
            # parse out suspected email gateway
            rmx = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9_-]*["
                             r"a-zA-Z0-9])?", mx_results)
            rmxval = re.findall(r"\.[a-zA-Z0-9]*\.[comi]{2,3}", str(rmx))
            if rmxval == ['.iphmx.com']:
                opf.write("\t " + mx_results + "\tCisco Secure Email Host\n")
                logging.info(mx_results + "\tCisco Secure Email Host")
            elif rmxval == ['.mimecast.com']:
                opf.write("\t " + mx_results + "\tMimecast Cloud Email Security Host\n")
                logging.info(mx_results + "\tMimecast Cloud Email Security Host")
            elif rmxval == ['.zixmail.net']:
                opf.write("\t " + mx_results + "\tPossibly Zixmail Host\n")
                logging.info(mx_results + "\tPossibly Zixmail Host")
            elif rmxval == ['.google.com']:
                opf.write("\t " + mx_results + "\tGoogle Workspaces Host\n")
                logging.info(mx_results + "\tGoogle Workspaces Host")
            elif rmxval == ['.outlook.com']:
                opf.write("\t " + mx_results + "\tO365 Email Host\n")
                logging.info(mx_results + "\tO365 Email Host")
            elif rmxval == ['.onmicrosoft.com']:
                opf.write("\t " + mx_results + "\tPossibly O365 Email Host\n")
                logging.info(mx_results + "\tPossibly O365 Email Host")
            elif rmxval == ['.zoho.com']:
                opf.write("\t " + mx_results + "\tZoho Cloud Email Host\n")
                logging.info(mx_results + "\tZoho Cloud Email Host")
            elif rmxval == ['.messagingengine.com']:
                opf.write("\t " + mx_results + "\tFastmail Cloud Email Host\n")
                logging.info(mx_results + "\tFastmail Cloud Email Host")
            elif rmxval == ['.amazonaws.com']:
                opf.write("\t " + mx_results + "\tAmazon WorkMail Cloud Email Host\n")
                logging.info(mx_results + "\tAmazon WorkMail Cloud Email Host")
            elif rmxval == ['.emailsvr.com']:
                opf.write("\t " + mx_results + "\tRackspace Cloud Office Host\n")
                logging.info(mx_results + "\tRackspace Cloud Office Host")
            elif rmxval == ['.spamtitan.com']:
                opf.write("\t " + mx_results + "\tSpamTitan Cloud Email Security Host\n")
                logging.info(mx_results + "\tSpamTitan Cloud Email Security Host")
            elif rmxval == ['.onice.io']:
                opf.write("\t " + mx_results + "\tIceWarp Cloud Email Host\n")
                logging.info(mx_results + "\tIceWarp Cloud Email Host")
            elif rmxval == ['.mxrecord.io']:
                opf.write("\t " + mx_results + "\tCloudflare Area 1 Email Security Host\n")
                logging.info(mx_results + "\tCloudflare Area 1 Email Security Host")
            elif rmxval == ['.messagelabs.com']:
                opf.write("\t " + mx_results + "\tSymantec Email Security.cloud Host\n")
                logging.info(mx_results + "\tSymantec Email Security.cloud Host")
            else:
                opf.write("\t" + mx_results + "\tUnrecognized Host\n")
                logging.info(mx_results + "\tUnrecognized Host")
    # if mx records not found...
    except:
        opf.write("[FAIL] MX Record Not Found.\n\n")
        logging.info("[FAIL] MX Record Not Found.")
        logging.warning("MX Record lookup has flat out FAILED.")
        pass
    # try looking for spf record
    try:
        logging.debug("trying to resolve TXT records for " + domain + "...")
        test_spf = dns.resolver.resolve(domain, 'TXT')
        logging.debug(test_spf)
        opf.write("\n")
        # look inside results, loop through w/regex to parse it out
        for spf_data in test_spf:
            logging.debug("trying to find TXT record containing string 'spf1'...")
            spf_results = str(spf_data)
            if 'spf1' in str(spf_data):
                logging.debug("'spf1' found...")
                opf.write("SPF Record Found:\n\t(Version, Allowed Hosts, All Else)\n\t" + spf_results + "\n")
                logging.info(spf_results)
                opf.write("\tSPF Details:\n")
                # regex for redirects
                try:
                    logging.debug("checking SPF record results for redirects...")
                    rredir = re.findall(r"(?i)[redict]{8}=(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                        r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rredirval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                           r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rredir))
                    if rredir == []:
                        opf.write("\t\t...Not Declared: Redirect.\n")
                        logging.info("...Not Declared: Redirect.")
                    else:
                        opf.write("\t\tRedirects to: " + str(rredirval) + "\n")
                        logging.info("Redirects to: " + str(rredirval))
                except:
                    pass

                # regex for includes
                try:
                    logging.debug("checking SPF record results for includes...")
                    rinc = re.findall(r"(?i)[include]{7}:(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?", spf_results)
                    rincval = re.findall(r"(?:[a-zA-Z0-9_-](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                         r"a-zA-Z0-9_-]*[a-zA-Z0-9])?", str(rinc))
                    if rincval == []:
                        opf.write("\t\t...Not Declared: Includes.\n")
                        logging.info("...Not Declared: Includes.")
                    else:
                        opf.write("\t\tIncludes: " + str(rincval) + "\n")
                        logging.info("Includes: " + str(rincval))
                except:
                    pass
                # regex for ipv4's??? COUNT???

                # regex for ipv6's??? COUNT???

                # regex for other macros??? UGH!!!
                try:
                    logging.debug("checking SPF record results for macros...")
                    rmac = re.findall(r"[%{]{2}[a-zA-Z][}]", spf_results)
                    if rmac == []:
                        opf.write("\t\t...Not Declared: Misc Macros.\n")
                        logging.info("...Not Declared: Misc Macros.")
                    else:
                        opf.write("\t\tMisc Macros: " + str(rmac) + "\n")
                        logging.info("Misc Macros: " + str(rmac))
                except:
                    pass

                # regex for all action CHAIN OF IF ELSE ELSE ELSE
                try:
                    logging.debug("checking SPF record results for All mechanism...")
                    rall = re.findall(r"(?i)[?+~-]all\"$", spf_results)
                    rallval = re.findall(r"[?+~-]", str(rall))
                    if rallval == ['?']:
                        opf.write("\t\tAll Mechanism: " + str(rallval) + " NEUTRAL.\n")
                        logging.info("All Mechanism: " + str(rallval) + " NEUTRAL.")
                    elif rallval == ['+']:
                        opf.write("\t\tAll Mechanism: " + str(rallval) + " PASS.\n")
                        logging.info("All Mechanism: " + str(rallval) + " PASS.")
                    elif rallval == ['~']:
                        opf.write("\t\tAll Mechanism: " + str(rallval) + " SOFTFAIL.\n")
                        logging.info("All Mechanism: " + str(rallval) + " SOFTFAIL.")
                    elif rallval == ['-']:
                        opf.write("\t\tAll Mechanism: " + str(rallval) + " HARDFAIL.\n")
                        logging.info("All Mechanism: " + str(rallval) + " HARDFAIL.")
                    else:
                        opf.write("\t\t...Not Declared: All Mechanism.\n")
                        logging.info("...Not Declared: All Mechanism.")
                except:
                    pass
    # if no spf record found...
    except:
        opf.write("[FAIL] SPF Record Not Found.\n\n")
        logging.info("[FAIL] SPF Record Not Found.")
        logging.warning("SPF Record lookup has flat out FAILED.")
        pass
    # try looking for dmarc record
    try:
        logging.debug("trying to resolve TXT records for " + domain + "...")
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        logging.debug(test_dmarc)
        opf.write("\n")
        # look inside results, loop through w/regex to parse it out
        for dmarc_data in test_dmarc:
            logging.debug("trying to find TXT record containing string 'DMARC1'...")
            dmarc_results = str(dmarc_data)
            if "DMARC1" in str(dmarc_data):
                logging.debug("'DMARC1' found...")
                opf.write("DMARC Record Found:\n\t(Version, Tags)\n\t" + dmarc_results + "\n")
                logging.info(dmarc_results)
                opf.write("\tDMARC Details:\n")
                # DMARC RUA Recipient
                try:
                    logging.debug("checking DMARC record results for rua...")
                    rrua = re.findall(r"[a-zA-Z][a-zA-Z][aA]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rruaval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rrua))
                    if rruaval == []:
                        opf.write("\t\t...Not Declared: Reports Aggregate Recipient (rua=<user@domain.com>).\n")
                        logging.info("...Not Declared: Reports Aggregate Recipient (rua=<user@domain.com>).")
                    else:
                        opf.write("\t\tReports Aggregate Recipient: " + str(rruaval) + "\n")
                        logging.info("Reports Aggregate Recipient: " + str(rruaval))
                except:
                    opf.write("\tReports Aggregate Recipient Not Declared.\n")
                    logging.info("Reports Aggregate Recipient Not Declared.")
                # DMARC RUF Recipient
                try:
                    logging.debug("checking DMARC record results for ruf...")
                    rruf = re.findall(r"[a-zA-Z][a-zA-Z][fF]=[a-zA-Z]ailto:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.["
                                      r"a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+["
                                      r"a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", dmarc_results)
                    rrufval = re.findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@("
                                            r"?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:["
                                            r"a-zA-Z0-9-]*[a-zA-Z0-9])?", str(rruf))
                    if rrufval == []:
                        opf.write("\t\t...Not Declared: Reports Forensic Recipient (ruf=<user@domain.com>).\n")
                        logging.info("...Not Declared: Reports Forensic Recipient (ruf=<user@domain.com>).")
                    else:
                        opf.write("\t\tReports Forensic Recipient: " + str(rrufval) + "\n")
                        logging.info("Reports Forensic Recipient: " + str(rrufval))
                except:
                    opf.write("\tReports Forensic Recipient Not Declared.\n")
                    logging.info("Reports Forensic Recipient Not Declared.")
                # DMARC DKIM Alignment
                try:
                    logging.debug("checking DMARC record results for adkim...")
                    radkim = re.findall(r"(?i)[adkim]{5}=[sr];", dmarc_results)
                    radkimval = re.findall(r"[sS,rR]", str(radkim))
                    if radkimval == []:
                        opf.write("\t\t...Not Declared: DKIM Alignment (adkim=<s|r>).\n")
                        logging.info("...Not Declared: DKIM Alignment (adkim=<s|r>).")
                    else:
                        opf.write("\t\tDKIM Alignment Strict/Relaxed: " + str(radkimval) + "\n")
                        logging.info("DKIM Alignment Strict/Relaxed: " + str(radkimval))
                except:
                    opf.write("\tDKIM Alignment Not Declared.\n")
                    logging.info("DKIM Alignment Not Declared.")
                # DMARC SPF Alignment
                try:
                    logging.debug("checking DMARC record results for aspf...")
                    raspf = re.findall(r"(?i)[aspf]{4}=[sr];", dmarc_results)
                    raspfval = re.findall(r"[sS,rR]", str(raspf))
                    if raspfval == []:
                        opf.write("\t\t...Not Declared: SPF Alignment (aspf=<s|r>).\n")
                        logging.info("...Not Declared: SPF Alignment (aspf=<s|r>).")
                    else:
                        opf.write("\t\tSPF Alignment Strict/Relaxed: " + str(raspfval) + "\n")
                        logging.info("SPF Alignment Strict/Relaxed: " + str(raspfval))
                except:
                    opf.write("\tSPF Alignment Not Declared.\n")
                    logging.info("SPF Alignment Not Declared.")
                # DMARC Percentage Filtered
                try:
                    logging.debug("checking DMARC record results for pct...")
                    rpct = re.findall(r"(?i)[pct]{3}=[0-9]{2,3}", dmarc_results)
                    rpctval = re.findall(r"[0-9]{2,3}", str(rpct))
                    if rpctval == []:
                        opf.write("\t\t...Not Declared: Percentage Msgs Filtered (pct=<0-100>).\n")
                        logging.info("...Not Declared: Percentage Msgs Filtered (pct=<0-100>).")
                    else:
                        opf.write("\t\tPercentage Msgs Filtered: " + str(rpctval) + "\n")
                        logging.info("Percentage Msgs Filtered: " + str(rpctval))
                except:
                    opf.write("\tPercentage Msgs Filtered Not Declared.\n")
                    logging.info("Percentage Msgs Filtered Not Declared.")
                # DMARC Subdomain Policy Action
                try:
                    logging.debug("checking DMARC record results for sp...")
                    rsp = re.findall(r"(?i)[sp]{2}=[a-zA-Z]*;", dmarc_results)
                    rspval = re.findall(r"[a-zA-Z]{4,10}", str(rsp))
                    if rspval == []:
                        opf.write("\t\t...Not Declared: Subdomain Policy Action (sp=<none|reject|quarantine>).\n")
                        logging.info("...Not Declared: Subdomain Policy Action (sp=<none|reject|quarantine>).")
                    else:
                        opf.write("\t\tSubdomain Policy Action: " + str(rspval) + "\n")
                        logging.info("Subdomain Policy Action: " + str(rspval))
                except:
                    opf.write("\tSubdomain Policy Action Not Declared.\n")
                    logging.info("Subdomain Policy Action Not Declared.")
                # DMARC Policy Action
                try:
                    logging.debug("checking DMARC record results for p...")
                    rp = re.findall(r"(?i)[p]=[a-zA-Z]*;", dmarc_results)
                    rpval = re.findall(r"[a-zA-Z]{4,10}", str(rp))
                    if rpval == []:
                        opf.write("\t\t...Uh Oh! Not Declared: Policy Action (p=<none|reject|quarantine>).\n")
                        logging.info("...Uh Oh! Not Declared: Policy Action (p=<none|reject|quarantine>).")
                    else:
                        opf.write("\t\tPolicy Action: " + str(rpval) + "\n")
                        logging.info("Policy Action: " + str(rpval))
                except:
                    opf.write("\tPolicy Action Not Declared.\n")
                    logging.info("Policy Action Not Declared.")
    # if no dmarc record found...
    except:
        opf.write("[FAIL] DMARC Record Not Found.\n\n")
        logging.info("[FAIL] DMARC Record Not Found.")
        logging.warning("DMARC Record lookup has flat out FAILED.")
        pass

opf.close()
logging.debug("closing " + outputfile + "...")
logging.info("please check directory for report " + outputfile + " to view txt file results.")
logging.debug("waiting for user input to exit...")
input("\nPress enter to exit ")
logging.debug("user input accepted. exiting...")
