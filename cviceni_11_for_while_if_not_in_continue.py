
# definuje slovník
temata = {
    "zvire": "kočka",
    "nabytek": "stůl"
    }

# vytiskne úvod
print("Toto jsou témata, která můžete hádat:")
print("----------------------------------------")

# vytiskne možná témata
for tema in temata:
    print(tema)
print("----------------------------------------")

# vyzve k zadání tématu
while True:
    zvolene_tema = input("Zadejte téma, které chcete zkusit uhodnout: ")
    if not zvolene_tema in temata:
        continue
    tip = input("Zadejte svůj tip: ")
    if tip == temata.get(zvolene_tema):
        print("Uhodl jste!!")
        exit()
