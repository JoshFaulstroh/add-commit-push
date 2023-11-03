import os
import sys
import time

print("Starting.")
time.sleep(0.5) 
numOfArgs = len(sys.argv)
print("Total Arguments Passed:", numOfArgs)
message = "Default commit"


print(message)

os.system("git status")
print("Continue? type 'y' for yes, 'n' for no.")
confirm = input()
if confirm == "n":
    print("terminating...")
    quit()

commitM = '\ngit commit -m "' +  message + '"'
print(commitM)
os.system(commitM)
os.system("git add .")
os.system("git status")
os.system("git push")