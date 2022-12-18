#1-import string module
#2-store all characters in lists (upper/;owercase, digits, punctuation)
#3-take number of characters from user as an input
#4-make sure the number of characters is 6 or more 
#5-shuffle all the lists
#6-calculate the precentages of the characters in the password
#create the password

import string
import random
l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

characters_number = input("How many characters should the password have?")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 8 :
            print("Password should have at least 8 characters!")
            characters_number = input("Please enter again, how many characters should the password have?")
        else:
            break
    except:
        print("Please enter numbers only!")
        characters_number = input("How many characters should the password have?")


random.shuffle(l1)       
random.shuffle(l2)     
random.shuffle(l3)     
random.shuffle(l4)      

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
5
password = []

for i in range(part1):
    password.append(l1[i])
    password.append(l2[i])

for i in range(part2):
    password.append(l3[i])
    password.append(l4[i])  


random.shuffle(password)

password = "".join(password[0:])


print(password)

#end of program