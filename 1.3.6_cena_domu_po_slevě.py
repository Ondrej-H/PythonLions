
# Uloží od uživatele cenu domu před slevou a výši slevy v procentech
cena_domu_pred_slevou = float(input('Zadejte cenu domu před slevou: '))
sleva_na_dum = float(input('Zadejte slevu na dům (v procentech): '))

# Vypočítá slevu
sleva_kc = (sleva_na_dum / 100) * cena_domu_pred_slevou
cena_po_sleve = cena_domu_pred_slevou - sleva_kc

# Vypíše výsledky
print(f'Cena domu před slevou je {cena_domu_pred_slevou}, sleva je {sleva_na_dum} %')
print(f'Sleva na dům: {sleva_kc}, Cena domu po slevě: {cena_po_sleve}')
