
# vytvoří řetězec ahoj svete a vypíše jej
muj_string = "   Ahoj, světe!   "
print(f"Původní věta: {muj_string}")

# odstraní bílé znaky z počátku a konce a vypíše výsledek
text_bez_mezer = muj_string.strip()     # lstrip() - odstraní všechny bílé znaky zleva      # rstrip( - odstraní všechny bílé znaky zprava)
print(f"Text bez bílých znaků na začátku a na konci: {text_bez_mezer}")