
# zadá cenu za kamenivo
cena = 500

# Vypíše ceny od 1 m3 do 5 m3
for m3 in range(1, 6):
    cena_kamenivo = m3 * cena
    print(f"Za {m3} m3 kameniva zaplatíme {cena_kamenivo} Kč")
