import os
import sys
import time

print("Starting...")
time.sleep(0.5) 
numOfArgs = len(sys.argv)
print("Total Arguments Passed:", numOfArgs)

os.system("git status")
print("Continue? Y or N")
confirm = input()
if confirm == "n":
    print("terminating...")
    quit()

message = input("Please provide commit message:")
print("Commit message entered:", message, "Is this correct? Y or N")
messageconfirm = input()
if messageconfirm == "n":
    correctedMessage = input("please provide commit message:")


commitM = '\ngit commit -m "' +  message + '"'
os.system("\n"+commitM)
os.system("\ngit add .")
os.system("\ngit status")
os.system("\ngit push")
print("...Finished")