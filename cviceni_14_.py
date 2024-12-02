
# vytvoří slovník "potraviny" a vypíše jej
potraviny = {
    "zelenina": {
        "rajce": 3,
        "okurka": 5
    },
    "ovoce": {
        "jablko": 10,
        "hruška": 8
    },
    "bobule": {
        "maliny": 100,
        "ostružiny": 50
    }
}
print(f"Původní slovník: {potraviny}")

# odstraní vnořený slovník "zelenina" a vypíše aktualizovaný slovník
del potraviny["zelenina"]
print(f"První odebírání: {potraviny}")

# vyprázdní celý slovník a vypíše aktualizovaný slovník
potraviny.clear()
print(f"Poslední odebírání (odebere vše): {potraviny}")

# pomocí escape sekvencí vypíše hlášku na dva řádky
print("Byl odstraněn celý obsah slovníku s názvem \"potraviny\" \nzde začíná nový řádek")

