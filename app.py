from style import estilo, linha, linhas
from opt import main
from calc_model import multiplication, division, sum, sub

estilo('Virtual Calculator v1.0')

main()
linha()
opc = int(input('Enter a option: '))

while True:
    if opc == 1:
        linhas('MULTIPLICATION')
        multiplication()
        print()
        cont = int(input('0 to continue or 1 to back menu: '))
        if cont == 1:
            estilo('Virtual Calculator v1.0')
            main()
            linha()
            opc = int(input('Enter a option: '))
            linha()
            print()
    elif opc == 2:
        linhas('DIVISION')
        division()
        print()
        cont = int(input('0 to continue or 1 to back menu: '))
        if cont == 1:
            estilo('Virtual Calculator v1.0')
            main()
            linha()
            opc = int(input('Enter a option: '))
            linha()
            print()
    elif opc == 3:
        linhas('SUM')
        sum()
        print()
        cont = int(input('0 to continue or 1 to back menu: '))
        if cont == 1:
            estilo('Virtual Calculator v1.0')
            main()
            linha()
            opc = int(input('Enter a option: '))
            linha()
            print()
    elif opc == 4:
        sub()
    elif opc == 5:
        break
    else:
        print('Error: Invalid option, enter a valid one!!!')
        opc = int(input('Enter a option: '))
estilo('Thank u, come back')