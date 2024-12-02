
# nastaví maximální obsah a počáteční stranu čtverce
max_obsah = int(input("Zadej maximální obsah: "))
strana_ctverce = int(input("Zadej stranu čtverce: "))

# vypočítá obsah čtverce (S = a * a)
obsah = strana_ctverce**2

# pomocí cyklu while vypíše obsah čtverce při zvětšování strany o 1 a menším obsahu než 100
while obsah < max_obsah:
    print(f"Obsah čtverce o straně {strana_ctverce} je {obsah}")
    strana_ctverce += 1
    obsah = strana_ctverce**2