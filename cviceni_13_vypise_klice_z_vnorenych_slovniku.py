
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
print(potraviny)
print("----------------------------------------")

print("Slovník obsahuje následující klíče:")
for hodnota in potraviny.values():
    for klic in hodnota:
        print(klic)

print("----------------------------------------")



