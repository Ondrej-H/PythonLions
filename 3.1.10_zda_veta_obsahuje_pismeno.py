
# načte od uživatele větu a hledané písmeno
veta = input("Napište libovolnou větu: ")
hledane_pismeno = input("Napište hledané písmeno: ")

# vytvoří pomocnou proměnou    # té se říká flag (příznak)
nalezeno = False

# pomocí cyklu for prohledá větu
for pismeno in veta:    # řetězec (str) je iterovatelný objekt
    if pismeno == hledane_pismeno: # pismeno.lower()
        nalezeno = True
        break               # účel programu už byl splněn, a tak program okasmžitě zastavíme pomocí break, abycho program zbytečně nespomalovali

# vypíše zda se ve větě písmeno nachází
if nalezeno:
    print(f"Zadaná věta '{veta}' obsahuje hledané písmeno '{hledane_pismeno}'")
else:
    print(f"Zadaná věta '{veta}' neobsahuje hledané písmeno '{hledane_pismeno}'")
