
print(9 // 2)

print(ord("a"))
print(ord("A"))


def secti_priority(seznam):
    soucet_priorit = 0
    priorita = 0
    for char in seznam:
        char = str(char)
        if char.islower():
            priorita = ord(char) - (ord('a') - 1)
            soucet_priorit += priorita
        elif char.isupper():
            priorita = ord(char) - (ord("A") - 27)
            soucet_priorit += priorita
    return soucet_priorit


l = ["p"]
print(secti_priority(l))


#for i in range (ord("a"), (ord("z") + 1)):
#    print(chr(i), end="")