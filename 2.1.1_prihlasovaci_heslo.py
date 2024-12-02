
# vytvoří/definuje heslo
heslo = 'tajne'

# načte heslo od uživatele
zadani_hesla = input('Zadejte heslo: ')

# kontrola hesla (rozhodovací blok)
if zadani_hesla == heslo:             # if zadani_hesla == 'tajne'
    print('Vítejte!')
else:
    print('Neplatné heslo. Přístup odepřen.')