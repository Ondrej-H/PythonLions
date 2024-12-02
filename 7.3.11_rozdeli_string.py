
# definuje větu a vypíše ji
veta = "Ahoj světe, ahoj pythone!"
print(f"Prohledávaná věta: {veta}")

# rozdělí stringy a vypíše seznam s částečnými stringy
seznam = veta.split(",") #veta.split(sep=",")
print(f"Seznam rozdělených pozdravů: {seznam}")

# definuje první částečný pozdrav a vypíše jej
pozdrav_1 = seznam[0]
print(f"Pozdrav 1: {pozdrav_1}")

# definuje druhý částečný pozdrav a vypíše jej
pozdrav_2 = seznam[1]
#pozdrav_2 = pozdrav_2.strip()
print(f"Pozdrav 2: {pozdrav_2}")
