
# importuje funkce secti() a odecti() z vlastního modulu - "funkce"
from matematicke_funkce.funkce import secti as s, odecti as o     # importuje samotné funkce secti() a odecti() jako funkce s() a o()

# zavolá funkci secti() z modulu "funkce" a vypíše výsledek
print(f"Součet čísel 5 + 3: {s(3,5)}")  # můžeme volat samotnou funkci, protože je importovaná přímo

# zavolá funkci odecti() z modulu "funkce" a vypíše výsledek
print(f"Rozdíl čísel 5 - 3: {o(5,3)}")
