

# definuje funkci pro vytvoření věty
def klicove_argumenty(jmeno, povolani, vek):
    return f"{jmeno} je {povolani} a je jí/mu {vek} let."


# zavolá funkci se třemi klíčovými argumenty
print(klicove_argumenty(vek=30, jmeno="Petr", povolani="programátor"))
