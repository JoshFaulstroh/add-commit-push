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
    correctedMessageconfirm = input()


commitM = '\ngit commit -m "' +  message + '"'
os.system(commitM)
os.system("git add .")
os.system("git status")
os.system("git push")
print("...Finished")