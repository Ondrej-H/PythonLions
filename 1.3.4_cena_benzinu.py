
# Uloží od uživatele cenu benzinu za litr a natankované množství
cena_litr = float(input('Zadejte cenu benzínu: '))
mnozstvi = float(input('Zadejte množství natankovaného benzínu: '))


# Vypočítá celkovou cenu benzinu
celkova_cena = cena_litr * mnozstvi


# Vypíše finální cenu, množství a cenu za litr
print('Celková cena je: ', celkova_cena, 'kč')
print('Natankováno bylo: ', mnozstvi, 'litrů')
print('Cena za litr je: ', cena_litr, 'kč')