orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

juft_buyurtmalar = []

for order in orders:
    if order[0] % 2 == 0:
        juft_buyurtmalar.append(order)

print(juft_buyurtmalar)
