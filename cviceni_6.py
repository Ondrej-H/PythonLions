
# vytvoří seznam nábytku a vypíše jej
seznam_nabytku = ["stůl", "židle", "skříň", "polička", "noční stolek"]
print(f"Počáteční seznam nábytku: {seznam_nabytku}")

# načte od uživatele počáteční a koncový index a vypíše příslušné prvky ze seznamu
pocatecni_index = int(input("Zadejte počáteční index rozsahu: "))
koncovy_index = int(input("Zadejte koncový index rozsahu: "))

novy_seznam_nabytku = seznam_nabytku[pocatecni_index:koncovy_index]
print(f"Prvky na požadovaném rozsahu jsou: {novy_seznam_nabytku}")

