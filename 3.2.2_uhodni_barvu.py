
# dotazuje se na barvu a vyhodnocuje odpověď dokud není zadanáˇsprávná odpově (zelená)
splneno = False

while splneno == False:
    zadana_barva = input("Uhodni barvu: ")
    if zadana_barva == "zelená":
        splneno = True
        print("Správně! Uhodl jsi barvu!")
    else:
        print("Špatně, hádej znovu!")