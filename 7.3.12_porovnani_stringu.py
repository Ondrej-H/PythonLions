
# načte od uživatele první a druhý řetězec
retezec_1 = input("Zadejte první řetězec: ")
retezec_2 = input("Zadejte druhý řetězec: ")

# vypíše vstupní řetězce
print(f"Vstupní řetězce jsou: \"{retezec_1}\" a \"{retezec_2}\"")

# provná vstupní řetězce
if retezec_1 == retezec_2:
    print("Stringy jsou stejné.")
else:
    print("Stringy nejsou stejné.")

# 2. varianta porovnání vstupních řetězců
if retezec_1 != retezec_2:
    print("Stringy nejsou stejné.")
else:
    print("Stringy jsou stejné.")
