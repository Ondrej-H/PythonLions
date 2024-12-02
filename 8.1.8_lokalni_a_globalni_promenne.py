
# vytvoří globální proměnnou a vypíše
globalni_promenna = 10
print(f"Globální proměnná na začátku: {globalni_promenna}")

# definuje funkci s lokální proměnnou a vypíše
def lokal():
    lokalni_promenna = 5
    print(f"Lokální proměnná ve funkci: {lokalni_promenna}")
    return lokalni_promenna


# zavolá funkci a uloží do globální proměnné návratovou hodnotu z funkce a vypíše
globalni_promenna = lokal()
print(f"Globální proměnná po přepsání: {globalni_promenna}")
