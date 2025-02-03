
# definuje funkci hraj
def hraj(hrac_1, hrac_2):
    if hrac_1 == hrac_2:
        print("Remíza!")
    elif (hrac_1, hrac_2) == ("kámen", "nůžky") or \
        (hrac_1, hrac_2) == ("nůžky", "papír") or \
        (hrac_1, hrac_2) == ("papír", "kámen"):
        print("Vyhrál hráč 1!")
    else:
        print("Vyhrál hráč 2!")

# načte vstup od uživatele
hrac_1 = input("Hráč 1: ")
hrac_2 = input("Hráč 2: ")

# zavolá funkci
hraj(hrac_1, hrac_2)

# kámen > nůžky
# nužky > papír
# papír > kámen