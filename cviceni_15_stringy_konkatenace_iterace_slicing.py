
# definuje proměnné retezec_a a retezec_2 a oddělovač
oddelovac = "-" * 20
retezec_1 = "abc"
retezec_2 = "def"

# a vypíše
print(oddelovac)
print(f"Řetězec 1: {retezec_1}")
print(f"Řetězec 2: {retezec_2}")
print(oddelovac)

# konkatenuje oba řetězce a vypíše
konkatenovany_retezec = retezec_1 + retezec_2
print(f"Konkatenovaný řetězec: {konkatenovany_retezec}")

# 3x iteruje konkatenovaný řetězec
iterovany_retezec = 3 * konkatenovany_retezec
print(f"Iterovaný řetězec: {iterovany_retezec}")

# pomocí slicingu vyřízne prostřední sekvenci z iterovaneho řetězce
vyriznuty_retezec = iterovany_retezec[6:12]
print(f"Vyříznutý řetězec (prostřední část z původního): {vyriznuty_retezec}")

