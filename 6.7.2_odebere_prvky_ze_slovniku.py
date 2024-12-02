
# vytvoří slovník a vypíše jej
slovnik_povolani = {
    "jmeno": "Jan",
    "vek": 30,
    "povolani": "junior programátor"
}
print(f"Počáteční slovník: {slovnik_povolani}")

# načte od uživatele prvek, který chce ze slovníku odebrat
odstranovany_klic = input("Zadejte klíč, který chcete odstranit: ")

# odebere prvek a vypíše aktualizovaný slovník
if odstranovany_klic in slovnik_povolani:       # kontrola výskytu klíče ve slovníku
    del slovnik_povolani[odstranovany_klic]
    print(f"Aktualizovaný slovník: {slovnik_povolani}")
else:
    print(f"Klíč {odstranovany_klic} není ve slovníku (tedy nelze odstranit)!")












