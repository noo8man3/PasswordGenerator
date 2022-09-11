#
#TODO
#ask user how many characters they want their password to be
#generate random characters up to that length
#output password
#

import random
import string

print("How many characters should this password be?: ")

pwdLength = input()
pwdLength = int(pwdLength) #convert str to int

pwdRaw = random.choices(string.printable, k=pwdLength)
genList = random.sample(pwdRaw, pwdLength)

pwd = ""

for i in range(0, len(genList)):
    pwd = pwd + (genList[i])
    
print("Here's your generated password: " + pwd)
