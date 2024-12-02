
def secti(a, b):
    """
    Sečte první a druhé číslo.\n
    :param a: první číslo\n
    :param b: druhé číslo
    """
    return a + b


def odecti(a, b):
    return a - b


def vynasob(a, b):
    return a * b


def vydel(a, b):
    if b == 0:
        print("Nulou nelze dělit!")     # raise ValueError("Nulou nelze dělit!")
    else:
        return a / b
