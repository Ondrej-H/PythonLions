
# 
# vytvoří řetězec ahoj svete a vypíše jej
muj_string = "Ahoj, svete!"
print(f"Prohledávaná věta: {muj_string}")

# načte od uživatele text pro který chce zjistit počet výskytů
hledany_text = input("Zadejte text, pro který chcete zjistit počet výskytů: ")

# zjistí kolikrát se daný text v řetězci nachází a vypíše
pocet_vyskytu = muj_string.count(hledany_text)
print(f"Text '{hledany_text}' se ve větě vyskytuje {pocet_vyskytu}x.")
