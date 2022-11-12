""" version 0.1, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver

domain = input("Enter a domain to check: ")


def spf_check(domain):
    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        print("######################")
        for spf_data in test_spf:
            if 'spf1' in str(spf_data):
                print("# SPF record found:\n#\t", spf_data)
                if "redirect=" in str(spf_data):
                    print("# \tA Redirect was found")
                if "include:" in str(spf_data):
                    print("# \tAn Include was found")
                if "+all" in str(spf_data):
                    print("# \tSPF ALL mechanism: +all (PASS)")
                elif "?all" in str(spf_data):
                    print("# \tSPF ALL mechanism: ?all (NEUTRAL)")
                elif "~all" in str(spf_data):
                    print("# \tSPF ALL mechanism: ~all (SOFTFAIL)")
                elif "-all" in str(spf_data):
                    print("# \tSPF ALL mechanism: -all (HARDFAIL)")
                else:
                    print("# \tSPF ALL mechanism: unknown")
    except:
        print("# [FAIL] SPF record not found.")
        pass


def dmarc_check(domain):
    try:
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        print("######################")
        for dmarc_data in test_dmarc:
            if "DMARC1" in str(dmarc_data):
                print("# DMARC record found:\n#\t", dmarc_data)
                if "p=reject" in str(dmarc_data):
                    print("# \tDMARC policy: reject")
                elif "p=quarantine" in str(dmarc_data):
                    print("# \tDMARC policy: quarantine")
                elif "p=none" in str(dmarc_data):
                    print("# \tDMARC policy: none")
                else:
                    print("# \tDMARC policy: unknown")

    except:
        print("# [FAIL] DMARC record not found.")
        pass


try:
    test_mx = dns.resolver.resolve(domain, "MX")
    print("######################")
    print("# MX records found:")
    for mx_data in test_mx:
        print("# \t", mx_data)
    spf_check(domain)
    dmarc_check(domain)
except:
    print("# [FAIL] MX record not found.")
    pass
