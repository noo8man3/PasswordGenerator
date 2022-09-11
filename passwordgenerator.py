#
#TODO
#ask user how many characters they want their password to be
#generate random characters up to that length
#output password
#

import random
import string

print("How many characters should this password be?: ")
pwdLength = int(input())
genList = random.choices(string.printable, k=pwdLength)
print("Here's your generated password: " + ''.join(genList))
