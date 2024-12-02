
# vytvoří slovník a vypíše jej
slovnik_povolani = {
    "jmeno": "Monika",
    "povolani": "kuchařka",
    "hobby": ["zahrada", "zvířata", "pletení"]
}
print(f"Počáteční slovník: {slovnik_povolani}")

# vytvoří seznam klíčů(z vytvořeného slovníku) a vypíše jej
seznam_klicu = list(slovnik_povolani.keys())
print(f"Seznam klíčů: {seznam_klicu}")





# ja jsem to dělal takto zbytečně složitě:
#seznam_klicu = []
#for key in slovnik_povolani:
#    seznam_klicu.append(key)

