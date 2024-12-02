
# vytvoří seznam stringů, vypíše je a vytvoří oddělovač
seznam_stringu = ["Ahoj", "světe,", "ahoj", "pythone!"]
print(f"Seznam samostatných řetězců: {seznam_stringu}")
oddelovac = " "

# spojí stringy do jednoho a vypíše výsledek
veta = oddelovac.join(seznam_stringu)    #veta = " ".join(map(str,seznam_stringu))
print(f"String po spojení: {veta}")





# jiná varianta
retezec = ""
for item in seznam_stringu:
    retezec += item + oddelovac

print(f"String po spojení: {retezec}")
