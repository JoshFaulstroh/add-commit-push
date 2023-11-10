import os
import sys
import time

print("\nStarting...")
time.sleep(0.5) 
numOfArgs = len(sys.argv)
print("\nTotal Arguments Passed:", numOfArgs)
#set up loop: set up variable (force) set to false by default
#if any command line arguments are '-f', change value of force to true
#Every confirmation should check force before querstion is asked, if force=true, don't ask questions


print("\ngit status\n")
time.sleep(0.5)
os.system("\ngit status")
time.sleep(0.5)
print("\nContinue? Y or N\n")
confirm = input()
if confirm == "n":
    print("\nterminating...\n")
    time.sleep(1)
    quit()

message = input("\nPlease provide commit message: ")
print("\nCommit message entered:", message, "Is this correct? Y or N\n")
messageconfirm = input()
if messageconfirm == "n":
    correctedMessage = input("\nplease provide commit message: ")


commitM = '\ngit commit -m "' +  message + '"'
time.sleep(0.5)
print("\nYour changes are about to be committed to your repository. Continue? Y or N\n")
commitConfirm = input()
if commitConfirm == "n":
    print("\nterminating...\n")
    time.sleep(1)
    quit()

print("\ngit commit", message, "\n")
time.sleep(0.5)
os.system("\n"+commitM)
time.sleep(0.5)

print("\nYou are about to perform the git add command. Continue? Y or N\n")
addConfirm = input()
if addConfirm == "n":
    print("\nterminating...\n")
    time.sleep(1)
    quit()
print("\ngit add .\n")
time.sleep(0.5)
os.system("\ngit add .")
time.sleep(0.5)

print("\ngit status\n")
time.sleep(0.5)
os.system("\ngit status")
time.sleep(0.5)

print("\nYou are about to perform the git push command. Continue? Y or N\n")
pushConfirm = input()
if pushConfirm == "n":
    print("\nterminating...\n")
    time.sleep(1)
    quit()
print("\ngit push\n")
time.sleep(0.5)
os.system("\ngit push")
time.sleep(0.5)

print("\n...Finished\n")
time.sleep(0.5)