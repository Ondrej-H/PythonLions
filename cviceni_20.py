
# definuje funkci
def argumenty(pozicni, klicovy, vychozi="vychozi"):
    print(f"Toto je první poziční argument: {pozicni}")
    print(f"Toto je první klíčový argument: {klicovy}")
    print(f"Toto je výchozí argument: {vychozi}")


# poprvé zavolá funkci
oddelovac = 15 * "-"
print(f"{oddelovac}1. volání funkce{oddelovac}")
argumenty("argument1", klicovy="argument2")

# po druhé zavolá funkci
print("---------------2. volání funkce---------------")
argumenty("argument1", klicovy="argument2", vychozi="vychozi_zmeneny")
