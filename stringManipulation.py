import sys

if len(sys.argv) == 2:
    print("Please enter your full name and last name as command line arguments.")
    sys.exit()

fullName = " ".join(sys.argv[1:])

email=fullName.lower().replace(" ",".")+"@google.com"

print(fullName)
print(email)
