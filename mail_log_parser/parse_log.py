
''' file extension types = .current && .s
Ex. 
Wed Sep 14 09:45:31 2022 Info: ICID 824107 Delayed HAT REJECT continuing session for recipient logging (10.8.236.135)
Wed Sep 14 09:45:31 2022 Info: ICID 824107 lost
Wed Sep 14 09:45:31 2022 Info: ICID 824107 close
Wed Sep 14 09:48:19 2022 Info: New SMTP ICID 824108 interface Data 1 (23.90.98.53) address 136.143.188.59 reverse dns host sender4-of-o59.zoho.com verified yes
Wed Sep 14 09:48:19 2022 Info: ICID 824108 ACCEPT SG ACCEPTLIST match sbrs[0.0:10.0] SBRS 3.4 country United States
Wed Sep 14 09:48:19 2022 Info: ICID 824108 TLS success protocol TLSv1.2 cipher ECDHE-RSA-AES256-GCM-SHA384
Wed Sep 14 09:48:20 2022 Info: Start MID 26983 ICID 824108
Wed Sep 14 09:48:20 2022 Info: MID 26983 ICID 824108 From: <noreply-dmarc@zoho.com>
Wed Sep 14 09:48:20 2022 Info: MID 26983 SDR: Domains for which SDR is requested: reverse DNS host: sender4-of-o59.zoho.com, helo: sender4-of-o59.zoho.com, env-from: zoho.com, header-from: Not Present, reply-to: Not Present
Wed Sep 14 09:48:20 2022 Info: MID 26983 SDR: Consolidated Sender Threat Level: Neutral, Threat Category: N/A, Suspected Domain(s) : N/A (other reasons for verdict). Sender Maturity: 30 days (or greater) for domain: sender4-of-o59.zoho.com
DTG = 1st 25chars
level = char26 to :
'''

# ask user for a keyword, pass keyword to value 'keyword'
keyword = input("What Keyword Would You Like to Find : ")

# open mail.current, read, for line in log_file look for keyword, print that line.
log_file = open("mail.current", "r")
for line in log_file:
    if keyword in line:
        print(line)
