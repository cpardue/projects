I need a way to submit a textfile list of email addresses to haveibeenpwned.com and see if each has been pwned or not.  
I need to be able to run this in windows, and may as well also import it to an executable with py2exe or something.  
I need API access and need to remember to not put my personal API key in github of course.  

Here's the pseudocode so far: 
# place textfile in same dir as executable
# run executable
# executable opens textfile
# for each line in textfile
#    query API for line
#    if pwned
#        print PWNED
#    else
#        print unlisted
# close textfile
# return 0
I guess it could possibly output an actual new textfile with the results as well, so you don't have to copy/paste it yourself.  
I don't know how to do that but i don't know how to do any of this, so...
