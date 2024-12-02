
# vytvoří slovník a vypíše jej (a mezeru)
slovnik = {
    "klic_1": "hodnota_1",
    "klic_2": "hodnota_2",
    "stejne_1": "stejne_1",
    "klic_3": "hodnota_3",
    "stejne_2": "stejne_2"
}
print(f"Slovník: {slovnik}")
print("")

# projde klíče ve slovníku, vezme hodnotu každého klíče a porovná s klíčem a vypíše příslušnou hlášku
for key in slovnik:
    hodnota = slovnik.get(key)
    print(f"{key} : {hodnota}")
    if key == hodnota:
        print("Klíč i hodnota jsou stejné!")
    else:
        print("Klíč a hodnota se liší!")
    print("")