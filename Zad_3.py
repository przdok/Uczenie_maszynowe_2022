def is_even(liczba: float) -> bool:
    return (liczba % 2) == 0

wynik = is_even(5)
if(wynik):
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')