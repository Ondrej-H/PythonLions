
# při zadání věty *a+h+o+j* *p+y+t+h+o+n+e* od uživatele -->
# --> vypíše ahoj pythone
veta = input("Zadej větu k rozšifrování: ")
znak = ""
for znak in veta:
    if znak == "*" or znak == "+":
        continue
    print(znak, end="")