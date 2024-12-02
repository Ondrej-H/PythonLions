
# vytvoří slovník s českým a anglickým názvem zvířete
zvirata = {
    "pes": "dog",
    "kočka": "cat",
    "lev": "lion"
}
print(f"Můj slovník zvířat: {zvirata}")

# postupně projde skrz všechny páry ve slovníku a vypíše
for klic, hodnota in zvirata.items():       # vytvoří tupl
    print(f"Česky: {klic}, Anglicky: {hodnota}")