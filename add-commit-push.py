import os
import sys

print("Add Commit Push Starting...") 
numOfArgs = len(sys.argv)
print("Total Arguments Passed:", numOfArgs)
message = "Default commit"
if numOfArgs == 3:
    if sys.argv[1] == "-m":    
        print("There are 3 arguments, p2 = -m")
    message = sys.argv[2] 

print(message)

print("Enter Your Name:")
x = input()
print("Hello,", x)

os.system("git status")
print("Continue? type 'y' for yes, 'n' for no.")
confirm = input()
if confirm != "y":
    print("terminating...")
    quit()

os.system("git add .")
os.system("git status")
os.system("git commit -m 'Default commit'")
os.system("git push")