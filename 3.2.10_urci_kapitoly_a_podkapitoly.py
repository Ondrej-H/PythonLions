
# načte počet kapitol a podkapitol
pocet_kapitol = int(input("Zadejte počet kapitol: "))
pocet_podkapitol = int(input("Zadejte počet podkapitol: "))

# hlavní cyklus - výpis kapitol
cislovani_kapitol = 1                           # nastaví proměnou pro hlavní cyklus
while cislovani_kapitol <= pocet_kapitol:       # cyklus pro číslování kapitol
    print(f"{cislovani_kapitol}. Kapitola")

    cislovani_podkapitol = 1
    # vnořený cyklus - výpis podkapitol
    while cislovani_podkapitol <= pocet_podkapitol:
        print(f"    {cislovani_podkapitol}. Podkapitola")
        cislovani_podkapitol += 1
    
    cislovani_kapitol += 1
