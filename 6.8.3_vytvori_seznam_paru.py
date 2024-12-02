# vytvoří slovník a vypíše jej
slovnik_povolani = {
    "jmeno": "Monika",
    "povolani": "kuchařka",
    "hobby": ["zahrada", "zvířata", "pletení"]
}
print(f"Počáteční slovník: {slovnik_povolani}")

# vytvoří seznam hodnot z vytvořeného slovníku a vypíše jej
seznam_hodnot = list(slovnik_povolani.items())
print(f"Seznam hodnot ze slovníku je: {seznam_hodnot}")