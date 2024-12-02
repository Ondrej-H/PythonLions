
# definuje funkci
def vypis(jmeno=None, vek=None, mesto=None):
    if jmeno is None or vek is None or mesto is None:
        print("Chybí některý z klíčových argumentů.")
    else:                       # častěji se používají escape sekvence \n než trojité úvozovky
        print(f"""Jméno: {jmeno}
Věk: {vek}
Město: {mesto}
""")


# poprvé zavolá funkci
vypis(jmeno="David")        # nebo: vypis() nebo: vypis(jmeno="David", mesto="Praha") atd.

# podruhé zavolá funkci
vypis(jmeno="David", vek=30, mesto="Praha")
