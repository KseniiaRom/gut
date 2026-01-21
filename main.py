print("Podaj a, a nastepnie b by kalkulator wykonal dzialania, kliknij enter po wprowadzeniu")
print("Nastepnie podaj znak dzialania (+,-,*,/)")
a = float ( input (’podaj A: ’) )
b = float ( input (’podaj B: ’) )
operacja = input (’podaj operacje : ’)

if operacja == ’+’:
    print(f’{a} + {b} = {a + b}’)
elif operacja == ’-’:
    print ( f’{a} - {b} = {a-b}’)