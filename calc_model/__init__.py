def multiplication():
    tot = 1
    num = []
    while True:
        n = int(input('Enter a number: '))
        num.append(n)
        tot *= n
        opc = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
        if opc not in 'YN':
            opc = str(input('Please: enter [Y/N] to continue: ')).strip().upper()[0]
        elif opc == 'N':
            break
    print(f'The numbers entered are {num} and their multiplication is equal to {tot}')

def division():
    while True:
        n1 = float(input('Numerator: '))
        n2 = float(input('Denominator: '))
        tot = n1 / n2
        print(f'The {n1} division to {n2} is equal to {tot}')

def sum():
    tot = 0
    num = []
    while True:
        n = float(input('Enter a number: '))
        num.append(n)
        tot += n
        opc = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
        if opc not in 'YN':
            opc = str(input('Please: enter [Y/N] to continue: ')).strip().upper()[0]
        elif opc == 'N':
            break
    print(f'The numbers entered are {num} and their sum is equal to {tot}')