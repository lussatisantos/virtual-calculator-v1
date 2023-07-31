def multiplication():
    """
    This def to numbers multiplication.

    Don't receive params, every account is doable within def
    All value are entered to loop, var NUM receive and put on list and var TOT multi all and show results
    """
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
    print()
    print(f'The numbers entered are {num}')
    print(f'Multiplication is equal to {tot}')

def division():
    while True:
        n1 = float(input('Numerator: '))
        n2 = float(input('Denominator: '))
        tot = n1 / n2
        print(f'The {n1} division to {n2} is equal to {tot}')
        opc = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
        if opc not in 'YN':
            opc = str(input('Please: enter [Y/N] to continue: ')).strip().upper()[0]
        elif opc == 'N':
            break

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
    
def sub():
    num = []
    while True:
        n = float(input('Enter a number: '))
        num.append(n)
        tot = n
        nume = tot - n
        opc = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
        if opc not in 'YN':
            opc = str(input('Please: enter [Y/N] to continue: ')).strip().upper()[0]
        elif opc == 'N':
            break
    print(f'The numbers entered are {num} and their sum is equal to {tot}')