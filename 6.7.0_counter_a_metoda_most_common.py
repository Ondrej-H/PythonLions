from collections import Counter

# Vstupní seznam jmen
names = [
    "Jan", "Marie", "Marek", "Jan", "Petra", 
    "Lukáš", "Jan", "Marie", "Marek", "Jan", 
    "Petra", "Marie", "Jan", "Jan", "Lukáš", 
    "Marek", "Petra", "Marie", "Jan", "Marie"
]

# Zjistí počty výskytů jmen
name_counts = Counter(names)

print(f"\nCounter(names) vytvořil tento slovník s názvem name_counts seřazený od nejvyšší hodnoty k nejnižší: {name_counts}")

# Zjistí tři nejčastější počty výskytů
most_common_counts = name_counts.most_common()
print("\nMetoda .most_common() vytvořila ze slovníku name_counts list tuplů s názvem most_common_counts.")
print(f"Typ proměnné most_common_counts je: {type(most_common_counts)}")
print(f"List most_common_couts je: {most_common_counts}")

print(f"\nNejvyšší počet výskytů je v druhá hodnota([1]) v prvním (=nultém -> [0]) tuplu - zapíšeme jako most_common_counts[0][1]: {most_common_counts[0][1]}")

print(f"\nDruhý nejvyšší počet výskytů je v druhá hodnota v druhém ([1]) tuplu - zapíšeme jako most_common_counts[1][1]: {most_common_counts[1][1]}")

print(f"\nTřetí nejvyšší počet výskytů je v druhá hodnota v třetím ([2]) tuplu - zapíšeme jako most_common_counts[2][1]: {most_common_counts[2][1]}")

# Vypíše výsledky
print(f"{most_common_counts[0][1]} x se vyskytuje:")
for name, count in most_common_counts:
    if count == most_common_counts[0][1]:
        print(name)

print(f"\n{most_common_counts[1][1]} x se vyskytuje:")
for name, count in most_common_counts:
    if count == most_common_counts[1][1]:
        print(name)

print(f"\n{most_common_counts[2][1]} x se vyskytuje:")
for name, count in most_common_counts:
    if count == most_common_counts[2][1]:
        print(name)