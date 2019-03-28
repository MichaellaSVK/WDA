# v súbore modulu si definujeme jednoduché funkcie
def non_zero(x):
    """Funkcia testuje, či je hodnota parametra x nenulová"""
    return x != 0       # vráti sa True ak x != 0, inak False

def is_positive(x):
    """Funkcia testuje, či je hodnota parametra x kladné číslo, alebo 0"""
    return x >= 0

# pri prvom importe sa vypíše aj nasledujúca správa
print("10 is positive?:", is_positive(10))