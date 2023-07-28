from style import estilo, linha, linhas
from opt import main
from calc_model import multiplication, division, sum, sub

estilo('Virtual Calculator v1.0')

main()
linha()
opc = int(input('Enter a option: '))

while True:
    if opc == 1:
        linhas('Multiplication')
        multiplication()
        cont = int(input('0 to continue or 1 to back menu: '))
        if cont == 1:
            opc = int(input('Enter a option: '))
    elif opc == 2:
        division()
    elif opc == 3:
        sum()
    elif opc == 4:
        sub()
    elif opc == 5:
        break
    else:
        print('Error: Invalid option, enter a valid one!!!')
        opc = int(input('Enter a option: '))
linhas('Thank u, come back')