''' !!! Keep It Simple, boi !!! '''

# ask user for path/to/logfile.name, pass value to log_file

# ask user for a keyword, pass keyword to value 'keyword'
keyword = input("What Keyword Would You Like to Find : ")

# open mail.current, read, for line in log_file look for keyword, print that line.
log_file = open("mail.current", "r")
for line in log_file:
    if keyword in line:
        print(line)
