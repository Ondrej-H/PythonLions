
# Uloží rozměry obdelníku (strana a a strana b) a převede na desetinné číslo
a = input('Napište délku strany a obdelníku (místo desetinné čárky použijte tečku): ')
b = input('Napište délku strany b obdelníku (místo desetinné čárky použijte tečku): ')
a = float(a)
b = float(b)

# Vypočítá obvod a obsah obdelníku
obvod = 2 * (a + b)          # vypočítá obvod
obsah = a * b                # vypočítá obsah

# Vypíše délky stran a obvod a obsah obdélníku
print('Délka strany a obdelníku je: ', a)
print('Délka strany b obdélníku je: ', b)
print('Obvod obdélníku je: ', obvod)
print('Obsah obdélníku je: ', obsah)

# '''zkopírovat celý řádek lze když je kurzor na řádku a není nic označeno
# pomocí "ctrl + c" '''
