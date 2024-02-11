import string
import random

password_length = int(input("ENTER PASSWORD LENGTH : "))
print('''Choose character Set for Password from these:
1. Digits
2. Combination of Lower case and Upper case letters
3. Lower case Letters only
4. Upper case Letters only
5. Special character
6. Exit
''')

characterList = ""
# Getting character set for password
while (True):
    choice = int(input("Pick your choice : "))
    if choice == 1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.ascii_lowercase
    elif choice == 4:
        characterList += string.ascii_uppercase
    elif choice == 5:
        characterList += string.punctuation
    elif choice == 6:
        break
    else:
        print("Pick a valid option")
password = []
for i in range(password_length):
    random_character = random.choice(characterList)
    password.append(random_character)
print("The random pasword is", "".join(password))
