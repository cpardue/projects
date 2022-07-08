# ----------------------------------------------------
import os
import sys
#
#

# Current Menu: Name
# Path > To > This > Page
# Options: 
# 1. X
# 2. Y 
# 3. Z 
# 9. Go Back
# 0. Exit
# 
# Please select an Option, then press Enter! 
# >_
# 
# 
# ----------------------------------------------------
# 
# Build the splash menu
# 
# Predeclare functions here? Each need to header the Current Page Name and Path > To, and need to present their own options from within Function.
def Banner():
  os.system("echo clear")
  print("""
  #################################")
  #         _                     #")
  # ___ ___| |__   ___  ___  __ _ #")
  #/ __/ __| '_ \ / _ \/ __|/ _` |#")
  #\__ \__ \ | | |  __/\__ \ (_| |#")
  #|___/___/_| |_|\___||___/\__,_|#")
  #                               #")
  #################################")
  chris pardue, sshesa v2
  """)
  return
#
def OnStart(): # OnStart(Create blank stamped files)
  os.system("echo touch ./Hosts.txt") #   touch Hosts.txt
  os.system("echo touch ./Commands.txt") #   touch Commands.txt
  return
#
def MainMenu():
  print("Current Menu: Main Menu") 
  print("Main Menu") 
  print("Options:") #     Options: 
  print("1: View/Edit Hosts") #     1: View/Edit Hosts
  print("2: View/Edit Commands") #     2: View/Edit Commands
  print("3: Run Commands") #     3: Run Commands
  print("9: Help") #     9: Help
  print("0: Exit") #     0: Exit
  print("")
  input("Please select an Option, then press Enter!") #     Please select an Option, then press Enter!
  while input != 0: #       if user input = 0, Exit()
    if 1 #       elseif 1
      ViewEditHosts() #         ViewEditHosts()
    elif 2 #       elseif 2
      ViewEditCommands() #         ViewEditCommands()
    elif 3 #       elseif 3
      RunCommands() #         RunCommands()
    elif 9 #       elseif 9
      Help() #         Help()
  return
# 
def ViewEditHosts() # ViewEditHosts(open/edit files)
  Banner()#   Banner()
  print("Current Menu: View/Edit Hosts") #     Current Menu: View/Edit Hosts
  print("Main Menu > View/Edit Hosts") #     Main Menu > View/Edit Hosts
  print("Options:") #     Options: 
  print("1: View Hosts") #     1: View Hosts
  print("2: Add Hosts") #     2: Add Hosts
  print("3: Remove All Hosts") #     3: Remove All Hosts
  print("9: Go Back") #     9: Go Back
  print("0: Exit Application") #     0: Exit Application
  input("Please select an Option, then press Enter: ") #     ask for user input (validate for above #'s only) 
  while input != 0: #       if user input = 0, Exit()
    if 1 #       elseif 1
      Banner() #         Banner()
      print("Current Menu: View Hosts")
      print("Main Menu > View/Edit Hosts > View Hosts")
      os.system("echo cat Hosts.txt") #         print Hosts.txt
      input("Press Any Key to Return") #         print Press Any Key to Return
      return #           upon keypress, ViewEditHosts()
    elif 2 #       elseif 2
      Banner() #         Banner()
      print("Enter a Hostname then Press Enter")
      #with open(Hosts.txt, "w") as f: #             pop open, write, pop closed
        #f.write(input()) #           print Enter a single hostname to add, then press Enter! 
      return
    elif 3 #       elseif 3
      Banner() #         Banner()
        while input != 2: #         while input >= 2
          print("Current Menu: Remove All Hosts") #     Current Menu: View/Edit Hosts
          print("Main Menu > View/Edit Hosts > Remove All Hosts") #     Main Menu > View/Edit Hosts
          print("Options:") #     Options: 
          print("1: Remove All Hosts From List") #         print 1: Yes
          print("2: Go Back") #         print 2: No, Go Back
          input("Please select an Option, then press Enter: ") #         ask for input
          if input = 1 #           if input = 1
            os.system("echo rm ./Hosts.txt && touch ./Hosts.txt") #             del Hosts.txt && touch Hosts.txt        
          else
            return #         ViewEditHosts()
    elif 9 #       elseif 9
      MainMenu() #         MainMenu()
    else #       else 
      ViewEditHosts() #         ViewEditHosts()
#  
OnStart() # OnStart()
Banner() #   Banner()
MainMenu() # MainMenu()
#   Current Menu: Main Menu
#   Main Menu
#   print menu
#  
#   

# 
# ViewEditCommands(open/edit files)
#   Banner()
#   print menu
#     Current Menu: View/Edit Hosts
#     Main Menu > View/Edit Hosts
#     Options: 
#     1: View Commands
#     2: Add Commands
#     3: Remove Commands
#     9: Go Back
#     0: Exit Application
#     
#     Please select an Option, then press Enter! 
#     ask for user input (validate for above #'s only)
#       if user input = 0, Exit()
#       elseif 1
#       elseif 2
#       elseif 3
#       elseif 9
#       
# RunCommands(Exec commands against hosts)
# Exit(exit)
#   rename Hosts.txt -> Hosts_DateTime.txt
#   rename Commands.txt -> Commands_DateTime.txt
#   maybe print Are You Sure? y/n
# 
# 
# Run Banner()
# OnStart()
# MainMenu()
