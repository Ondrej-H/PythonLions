
# vytvoří řetězec ahoj svete a vypíše jej
muj_string = "Ahoj světe, ahoj pythone!"
print(f"Prohledávaná věta: {muj_string}")

# načte od uživatele text pro který chce zjistit index
hledany_text = input("Zadejte hledaný text: ")

# zjistí index hledaného textu
index = muj_string.find(hledany_text)    # v případě nenalezení vrací hodnotu -1

# vypíše na jakém indexu se hledaný text nachází
if hledany_text in muj_string:
    print(f"Text '{hledany_text}' začíná na indexu {index}")
else:
    print(f"Text '{hledany_text}' nebyl nalezen v řetězci.")

# 2. varianta               # 3. varianta       # 4. varianta (opačná - museli bychom prohodit výpisy)
if index == -1:             # if index < 0      # if index != -1
    print(f"Text '{hledany_text}' nebyl nalezen v řetězci.")
else:
    print(f"Text '{hledany_text}' začíná na indexu {index}")
