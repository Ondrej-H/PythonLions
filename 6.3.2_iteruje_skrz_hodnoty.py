
# vytvoří slovník s českým a anglickým názvem zvířete
zvirata = {
    "pes": "dog",
    "kočka": "cat",
    "lev": "lion"
}
print(f"Můj slovník zvířat: {zvirata}")

# postupně projde všechny hodnoty
for zvire in zvirata.values():
    print(f"Anglicky: {zvire}")


#for zvire in zvirata:
#    print(f"Anglicky: {zvirata.get(zvire)}")
