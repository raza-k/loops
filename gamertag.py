import random

names = ["joe", "monke", "fortnite", "sans" , "big", "bent"]
a = int(input("how many words do you want in your name:"))

for i in range(a):
    print(random.choice(names), end=" ")

print("")


