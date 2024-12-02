
# Uloží od uživatele cenu za 1kg jablek a 1 kg banánů a převede na desetinné číslo
cena_jablek = float(input('Zadejte cenu za 1 kg jablek: '))
cena_bananu = float(input('Zadejte cenu za 1 kg banánů: '))


# Porovná cenu jablek a banánů   # altgr , = <     altgr . = >
if cena_jablek < cena_bananu:
    print('Cena za jablka není větší než cena za banány.')
else:
    print('Cena za jablka je vetší než za banány.')

# Vypíše cenu za kilo jablek a banánů - 2 varianty stringu
print('Cena za kilo jablek je: ', cena_jablek, 'Cena za banány je: ', cena_bananu)
print(f'Cena za kilo jablek je {cena_jablek} a cena za banány je {cena_bananu}')

