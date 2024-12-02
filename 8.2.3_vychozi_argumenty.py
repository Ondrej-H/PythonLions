
# definuje funkci
def vitej(jmeno, pozdrav="Ahoj"):       # pozdrav jako výchozí (defaultní) argument nastaví na "Ahoj"
    return f"{pozdrav}, {jmeno}!"


# zavolá funkci - pouze s jedním argumentem
print(vitej("Petře"))

# zavolá funkci - se 2 argumenty
print(vitej("Alice", "Dobrý den"))
