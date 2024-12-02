
# Vytvoří a vypíše původní větu a oddělovač
puvodni_veta = "   ToTo Je PůVoDní VěTa"
print(f"Původní věta: {puvodni_veta}")
print(20 * "-")

# převede všechny písmena z původní věty na malá písmena
mala_pismena = puvodni_veta.lower()
print(f"Věta převedená na malá písmena: {mala_pismena}")

# odstraní přebytečné bílé znaky
bez_bilych_znaku = mala_pismena.strip()
print(f"Věta bez přebytečných bílých znaků: {bez_bilych_znaku}")

# vypíše počet výskytů pro podřetězec 'to'
pocet_vyskytu = bez_bilych_znaku.count("to")
print(f"Podřetězec 'to' se ve větě nachází {pocet_vyskytu} krát")
