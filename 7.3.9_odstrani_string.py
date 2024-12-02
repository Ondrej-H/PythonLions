
# vytvoří řetězec ahoj svete a vypíše jej
retezec = "Ahoj světe, ahoj pythone!"
print(f"Původní věta: {retezec}")

# načte od uživatele odstraňovaný text
odstranovany_text = input("Napište text, který chcete odstranit: ")

# odstraní text a vypíše zbytek
upraveny_retezec = retezec.replace(odstranovany_text, "")
print(f"Upravený řetězec: {upraveny_retezec}")
