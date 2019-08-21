import string
import random

'''
ALPHABETS :
'''

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = "0123456789"
specials = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

print("lowercase : %s" % lowercase)

print("uppercase : %s" % uppercase)

print("numbers : %s" % numbers)

print("specials : %s" % specials)

print("-" * 20)
print("" * 5 + "PASSWORD GENERATOR")
print()
print("-" * 20)
print("" * 5 + "Type every number of the type of character you want to include in your password (i.e. '24'")
print()
print("" * 5 + "1 : Lowercase characters")
print("" * 5 + "2 : Uppercase characters")
print("" * 5 + "3 : Numbers")
print("" * 5 + "4 : Special characters")
print()
print("-" * 20)
print()
choice = input(" >  ")

alphabet = ""

if "1" in choice:
    alphabet += lowercase

if "2" in choice:
    alphabet += uppercase

if "3" in choice:
    alphabet += numbers

if "4" in choice:
    alphabet += specials

print("-" * 20)
print("" * 5 + "How long do you want your password to be ?")
print()
print("-" * 20)
length = input(" >  ")

password = ""

for i in range(1, int(length)):
    j = random.randint(0, len(alphabet)-1)
    password += alphabet[j]

print("-" * 20)
print("" * 5 + "Congratulations, here is your password : %s" % password)
print()
print("-" * 20)
print()


