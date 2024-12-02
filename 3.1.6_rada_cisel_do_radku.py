
# vypíše řadu čísel(0 až 4) do jednoho řádku
for i in range(5):
    # end = " " nastaví u funkce print() že konec není konec řádku (což je defaultní nastavení), ale konec bude merzera
    print(i, i, end=" ", sep="-")  # sep vkládá řetězec mezi vypisované proměné


for x in range(5):
    for y in range(4):
        print(x, y, sep="-")