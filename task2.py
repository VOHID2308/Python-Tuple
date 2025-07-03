talabalar =  [
    ("Ali", ["Fizika", "Matematika"]),
     ("Laylo", ["Ingliz tili"]), 
     ("Jasur", ["Matematika", "Informatika"])
]

fan = input()

sanash = 0
for talaba in talabalar:
    if fan in talaba[1]:
        sanash += 1

print(sanash)