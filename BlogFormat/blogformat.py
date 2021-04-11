# banner
# import stuff
#
# HEADER
OLD_FILE = input("Name of the file to convert/post? :") # ask for name of file to be formatted as OLD_FILE
TITLE = input("Title for the post :") # ask for title then assign as TITLE
DATE = input("Date in yyyy-mm-dd format :") # ask for date (yyyy-mm-dd) then assign as DATE
SUMMARY = input("Summary of the post :") # ask for summary then assign SUMMARY
CATEGORIES = input("Categories :") # ask for category (show menu of 1-9 as options) then assign as CATEGORIES
TAGS = input("Tags :") # ask for tags (show menu of 1-9 as options) then assign as TAGS
NEW_FILE = DATE + "-" + TITLE + ".md" # create a new md file as DATE + TITLE .md
f = open(NEW_FILE, "w")
f.write("---\n")
f.write("layout:\tpost\n")
f.write("title:\t" + TITLE + "\n")
f.write("date:\t" + DATE + "\n")
f.write("summary:\t" + SUMMARY + "\n")
f.write("categories:\t" + CATEGORIES + "\n")
f.write("thumbnail:\tcogs\n")
f.write("tags:\n")
f.write(" - " + TAGS + "\n")
f.write("---\n")
f.close()
with open(OLD_FILE, 'r') as firstfile, open (NEW_FILE, 'a') as secondfile: # form header with above variables
    for line in firstfile:
        secondfile.write(line)
print("Formatted")
