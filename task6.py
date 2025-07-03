emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))

domenlar = []

for name, email in emails:
    domen = email.split("@")[1]
    domenlar.append(domen)

print(domenlar)
