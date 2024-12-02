
# definuje první a druhou množinu čísel a vypíše je
mnozina_1 = {1, 2, 3}
mnozina_2 = {3, 4, 5}
print(f"První množina je: {mnozina_1}")
print(f"První množina je: {mnozina_2}")

# vypíše oddělovač
print("--------------------")

# provede operace průnik, sjednocení, rozdíl a symetrický rozdíl
#prunik = mnozina_1.intersection(mnozina_2)
prunik = mnozina_1 & mnozina_2  # altgr + c [:antersant:] 

#sjednoceni = mnozina_1.union(mnozina_2)     # na pořadí nezáleží
sjednoceni = mnozina_1 | mnozina_2  # altgr + w [:svislítko:]

#rozdil = mnozina_1.difference(mnozina_2)    # záleží na pořadí
rozdil = mnozina_1 - mnozina_2

#symetricky_rozdil = mnozina_1.symmetric_difference(mnozina_2)
#symetricky_rozdil_2 = mnozina_2.symmetric_difference(mnozina_1)
symetricky_rozdil = mnozina_1 ^ mnozina_2 # altgr + 33



# vypíše výsledky
print(f"Průnik obou množin je: {prunik}")
print(f"Sjednocení obou množin je: {sjednoceni}")
print(f"Rozdíl první a druhé množiny (od první množiny odečítáme druhou) je: {rozdil}")
print(f"Symetrický rozdíl obou množin je: {symetricky_rozdil}")
#print(f"Symetrický rozdíl obou množin je: {symetricky_rozdil_2}")




