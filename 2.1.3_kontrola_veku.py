
# načte rok narození od uživatele
rok_narozeni = int(input('Zadejte rok narození uživatele: '))

# Spočítá věk uživatele
momentalni_rok = 2024
vek = momentalni_rok - rok_narozeni

# Porovná věk uživatele a vypíše hlášku
if vek >= 18:
    print('Uživatel je starší 18 let')
else:
    print('''Uživatel je mladší 18 let. 
Prodej alkoholu zakázán!''')

# Vypíše věk uživatele
print('Věk uživatele je: ', vek, 'let')
print(f'Věk uživatele je: {vek} let')