people : list[tuple[str, int]] = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

eng_kattasi = people[0]
for odam in people:
    if odam[1] > eng_kattasi[1]:
        eng_kattasi = odam

print(eng_kattasi)