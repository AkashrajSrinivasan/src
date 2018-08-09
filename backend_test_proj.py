import random
import string
l = []
a = []
size = int(input("Enter the size of string"))
point = 0
for i in range(size):
    s = random.choice(string.ascii_uppercase)
    l.append(s)
times = int(input("Enter how many chances you want"))
print("OK,Now enter the String")
while (times != 0):
    s = input().upper()
    for char in s:
        a.append(char)
    for e in a:
        if e in l:
            if a.index(e) == l.index(e):
                print("The letter {0} is in right position".format(e))
                point = point + 1
                if (
                        point == size
                ):  #IF USER GUESSED ALL THE CHARS IN CORRECT POSITION..THEN BREAK
                    break

            else:
                print("The letter {0} is guessed but not in right position".
                      format(e))
        else:
            print("Guess again")
    times = times - 1
    a *= 0
print(*l)
