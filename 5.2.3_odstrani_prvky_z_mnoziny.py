
# vytvoří množinu největších měst ČR a vypíše ji
mesta = set(["Praha", "Brno", "Ostrava"])
print(f"Původní množina měst: {mesta}")

# odebere Ostravu a vypíše aktualizovanou množinu           # try: except:
mesta.remove("Ostrava")     # metoda remove vyhodí KeyError, pokud se daný argument (zde "Ostrava") v množině nenachází
print(f"Množina měst bez Ostravy: {mesta}")

# odebere Brno a vypíše aktualizovanou množinu
mesta.discard("Brno")       # metoda discard nevyhodí chybu ani pokud se daný argument (zde "Ostrava") v množině nenachází
print(f"Množina měst bez Ostravy a Brna: {mesta}")