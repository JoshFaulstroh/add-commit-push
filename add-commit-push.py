import os
import sys
import time

print("\nStarting...")
time.sleep(0.5) 
numOfArgs = len(sys.argv)
print("\nTotal Arguments Passed:", numOfArgs)

print("\ngit status")
os.system("\ngit status")
print("\nContinue? Y or N")
confirm = input()
if confirm == "n":
    print("\nterminating...")
    time.sleep(1)
    quit()

message = input("\nPlease provide commit message:")
print("\nCommit message entered:", message, "Is this correct? Y or N")
messageconfirm = input()
if messageconfirm == "n":
    correctedMessage = input("\nplease provide commit message:")


commitM = '\ngit commit -m "' +  message + '"'
print("\ngit commit", message)
time.sleep(0.5)
os.system("\n"+commitM)
print("\ngit add .")
time.sleep(0.5)
os.system("\ngit add .")
print("\ngit status")
time.sleep(0.5)
os.system("\ngit status")
print("\ngit push")
time.sleep(0.5)
os.system("\ngit push")
print("\n...Finished")
time.sleep(0.5)