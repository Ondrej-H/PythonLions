
# definuje funkci s libovolným počtem klíčových argumenentů
def vypis(**kwargs):
    return kwargs       #vysledek = {}       # return kwargs
                        #for klic, hodnota in kwargs.items():
                        #    vysledek[klic] = hodnota
                        #return vysledek


# zavolá funkci
vysledek_slovnik = vypis(jmeno="Alice", vek=20, mesto="Praha", prijmeni="Nováková")

# vypíše výsledek (vytáhne klíče a hodnoty ze slovníku)
for klic, hodnota in vysledek_slovnik.items():
    print(f"{klic}: {hodnota}")
