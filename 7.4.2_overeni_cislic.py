
# získá vstup od uživatele (věk)
vek = input("Zadejte svůj věk: ")

# zkontroluje zda jsou všechny znaky v řetězci pouze číslice
#je_cislo = vek.isdigit()

#vek.isnumeric()

if vek.isdigit():
    print("Všechny znaky v řetězci jsou číslice.")
else:
    print("Alespoň jeden znak není číslice.")

# .isnumeric() přijímá krom 0 - 9 také:
# římské číslice, zlomky a tak podobně