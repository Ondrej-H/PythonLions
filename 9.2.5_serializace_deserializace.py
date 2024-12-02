
print(40*"-")
# importuje JSON
import json

# vytvoří seznam (klasický Python seznam) a vypíše jej
seznam = ["Matouš", "Marek", "Lukáš"]
print(f"Původní seznam: {seznam}")

# zakóduje do JSONu a vypíše
json_data = json.dumps(seznam)
print(f"Kódovaná data: {json_data}")

# vypíše typ JSON řetězce
print(type(json_data))  # funkce type() nám říká jakého je typu argument, který jí dáváme

# dekódování dat nazpět a výpis
dekodovany_seznam = json.loads(json_data)   # loads() == load string
print(f"Dekódovaný seznam: {dekodovany_seznam}")
