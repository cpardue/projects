""" version 0.1.4, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver
# import re

domain = input("Enter a domain to check: ")
outputfile = domain + ".txt"
with open(outputfile, "w") as opf:
    try:
        test_mx = dns.resolver.resolve(domain, "MX")
        opf.write("########################################\n")
        opf.write("# MX records found:\n#     Priority\tHostname\n")
        for mx_data in test_mx:
            print("# \t", mx_data)
            mx_results = str(mx_data)
            opf.write("# \t" + mx_results + "\n")
    except:
        print("# [FAIL] MX record not found.\n")
        opf.write("# [FAIL] MX record not found.\n")
        pass
    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        print("########################################\n")
        opf.write("########################################\n")
        for spf_data in test_spf:
            spf_results = str(spf_data)
            if 'spf1' in str(spf_data):
                print("# SPF record found:\n#\t", spf_data)
                opf.write("# SPF record found:\n#\t" + spf_results + "\n")
                if "redirect=" in str(spf_data):
                    print("# \tRedirect(s) found.\n")
                    opf.write("# \tRedirect(s) found.\n")
                if "include:" in str(spf_data):
                    print("# \tInclude(s) found.\n")
                    opf.write("# \tInclude(s) found.\n")
                if "+all" in str(spf_data):
                    print("# \tSPF ALL mechanism: +all (PASS).\n")
                    opf.write("# \tSPF ALL mechanism: +all (PASS).\n")
                elif "?all" in str(spf_data):
                    print("# \tSPF ALL mechanism: ?all (NEUTRAL).\n")
                    opf.write("# \tSPF ALL mechanism: ?all (NEUTRAL).\n")
                elif "~all" in str(spf_data):
                    print("# \tSPF ALL mechanism: ~all (SOFTFAIL).\n")
                    opf.write("# \tSPF ALL mechanism: ~all (SOFTFAIL).\n")
                elif "-all" in str(spf_data):
                    print("# \tSPF ALL mechanism: -all (HARDFAIL).\n")
                    opf.write("# \tSPF ALL mechanism: -all (HARDFAIL).\n")
                else:
                    print("# \tSPF ALL mechanism: unknown.\n")
                    opf.write("# \tSPF ALL mechanism: unknown.\n")
    except:
        print("# [FAIL] SPF record not found.")
        opf.write("# [FAIL] SPF record not found.\n")
        pass
    try:
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        print("########################################")
        opf.write("########################################\n")
        for dmarc_data in test_dmarc:
            dmarc_results = str(dmarc_data)
            if "DMARC1" in str(dmarc_data):
                print("# DMARC record found:\n#\t", dmarc_data)
                opf.write("# DMARC record found:\n#\t" + dmarc_results + "\n")
                if "p=reject" in str(dmarc_data):
                    print("# \tDMARC policy: reject.")
                    opf.write("# \tDMARC policy: reject.\n")
                elif "p=quarantine" in str(dmarc_data):
                    print("# \tDMARC policy: quarantine.")
                    opf.write("# \tDMARC policy: quarantine.\n")
                elif "p=none" in str(dmarc_data):
                    print("# \tDMARC policy: none.")
                    opf.write("# \tDMARC policy: none.\n")
                else:
                    print("# \tDMARC policy: unknown.")
                    opf.write("# \tDMARC policy: unknown.\n")

    except:
        print("# [FAIL] DMARC record not found.")
        pass
opf.close()
#input("\nPress enter to exit ")
