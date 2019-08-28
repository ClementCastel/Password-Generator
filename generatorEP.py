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

print("-" * 20)
print("" * 5 + "How long do you want your password to be ?")
print()
print("-" * 20)
length = input(" >  ")

print("choice %s" % choice)
password = ""

for i in range(1, int(length)):
    j = random.randint(0, len(choice)-1)
    j = choice[j]

    if str(j) == "1":
        k = random.randint(0, len(lowercase) - 1)
        password += lowercase[k]
    elif str(j) == "2":
        k = random.randint(0, len(uppercase) - 1)
        password += uppercase[k]
    elif str(j) == "3":
        k = random.randint(0, len(numbers) - 1)
        password += numbers[k]
    elif str(j) == "4":
        k = random.randint(0, len(specials) - 1)
        password += specials[k]

print("-" * 20)
print("" * 5 + "Congratulations, here is your password : %s" % password)
print()
print("-" * 20)
print()
