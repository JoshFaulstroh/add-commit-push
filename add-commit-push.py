import os
import sys
import time

print("\nStarting...")
time.sleep(0.5) 
numOfArgs = len(sys.argv)
print("\nTotal Arguments Passed:", numOfArgs)

print("\ngit status")
time.sleep(0.5)
os.system("\ngit status")
time.sleep(0.5)
print("\nContinue? Y or N\n")
confirm = input()
if confirm == "n":
    print("\nterminating...\n")
    time.sleep(1)
    quit()

message = input("\nPlease provide commit message:")
print("\nCommit message entered:", message, "Is this correct? Y or N\n")
messageconfirm = input()
if messageconfirm == "n":
    correctedMessage = input("\nplease provide commit message:")


commitM = '\ngit commit -m "' +  message + '"'
time.sleep(0.5)
print("\ngit commit", message, "\n")
time.sleep(0.5)
os.system("\n"+commitM)
time.sleep(0.5)
print("\ngit add .\n")
time.sleep(0.5)
os.system("\ngit add .")
time.sleep(0.5)
print("\ngit status\n")
time.sleep(0.5)
os.system("\ngit status")
time.sleep(0.5)
print("\ngit push\n")
time.sleep(0.5)
os.system("\ngit push")
time.sleep(0.5)
print("\n...Finished\n")
time.sleep(0.5)