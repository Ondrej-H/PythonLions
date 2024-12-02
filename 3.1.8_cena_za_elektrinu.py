
# uloží cenu paušálu a kwh
cena_pausalu = 370
cena_kwh = 3

# vypíše cenu za spotřebu 100 - 500 kwh
for i in range(100, 600, 100):
    cena = cena_kwh * i + cena_pausalu
    print(f"Cena za elektřinu {i} kwh je {cena} Kč")
