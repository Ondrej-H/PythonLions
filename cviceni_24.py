
# vytvoří třídu zvire s atributy rasa a jmeno
class Zvire():
    def __init__(self, rasa = None, jmeno = None):
        self.rasa = rasa
        self.jmeno = jmeno


# vytvoří instanci s atributy rasa="Kočka" a jmeno="Micka"
kocka = Zvire(rasa="Kočka", jmeno="Micka")
print(f"Rasa: {kocka.rasa}")
print(f"Jméno: {kocka.jmeno}")

# zjistí a vypíše datový typ třídy
print("Zjistí a vypíše datový typ třídy:")
print(type(kocka))
