""" version 0.11, by Chris Pardue, see chris-pardue.com
or github.com/cpardue for more sketchy python scripts"""
import dns.resolver

domain = input("Enter a domain to check: ")


def spf_check(domain):
    try:
        test_spf = dns.resolver.resolve(domain, 'TXT')
        for spf_data in test_spf:
            if 'spf1' in str(spf_data):
                print("SPF record found: ", spf_data)
                if "+all" in str(spf_data):
                    print("-->SPF ALL mechanism: +all (PASS)")
                elif "?all" in str(spf_data):
                    print("-->SPF ALL mechanism: ?all (NEUTRAL)")
                elif "~all" in str(spf_data):
                    print("-->SPF ALL mechanism: ~all (SOFTFAIL)")
                elif "-all" in str(spf_data):
                    print("-->SPF ALL mechanism: -all (HARDFAIL)")
                else:
                    print("-->SPF ALL mechanism: unknown")
    except:
        print("[FAIL] SPF record not found.")
        pass


def dmarc_check(domain):
    try:
        test_dmarc = dns.resolver.resolve("_dmarc." + domain, "TXT")
        for dmarc_data in test_dmarc:
            if "DMARC1" in str(dmarc_data):
                print("DMARC record found: ", dmarc_data)
                if "p=reject" in str(dmarc_data):
                    print("-->DMARC policy: reject")
                elif "p=quarantine" in str(dmarc_data):
                    print("-->DMARC policy: quarantine")
                elif "p=none" in str(dmarc_data):
                    print("-->DMARC policy: none")
                else:
                    print("-->DMARC policy: unknown")

    except:
        print("[FAIL] DMARC record not found.")
        pass


try:
    test_mx = dns.resolver.resolve(domain, "MX")
    for mx_data in test_mx:
        print("MX record found: ", mx_data)
    spf_check(domain)
    dmarc_check(domain)
except:
    print("[FAIL] MX record not found.")
    pass
