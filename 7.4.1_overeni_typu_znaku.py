
# získá vstup od uživatele (jméno)
jmeno = input("Zadejte své jméno: ")

# zkontroluje zda jsou všechny znaky v řetězci abecední
#je_abecedni = jmeno.isalpha()    # bool: True / False

if jmeno.isalpha():
    print("Všechny znaky v řetězci jsou abecední písmena.")
else:
    print("Alespoň jeden znak není abecední.")
