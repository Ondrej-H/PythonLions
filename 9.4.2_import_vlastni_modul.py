
# importuje vlastní modul - "funkce"
from matematicke_funkce import funkce   # importujeme celý modul funkce

# zavolá funkci secti() z modulu "funkce" a vypíše výsledek
print(f"Součet čísel 5 + 3: {funkce.secti(3,5)}")   # k funkcím z modulu přistupujeme přes tečku - modul.funkce() - (zde pod názvy funkce.secti())

# zavolá funkci odecti() z modulu "funkce" a vypíše výsledek
print(f"Rozdíl čísel 5 - 3: {funkce.odecti(5,3)}")
