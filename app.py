from style import estilo, linha
from opt import main
from calc_model import multiplication, division, sum, sub

estilo('Virtual Calculator v1.0')

main()
linha()
opc = int(input('Enter a option: '))

if opc == 1:
    multiplication()
elif opc == 2:
    division()
elif opc == 3:
    sum()
elif opc == 4:
    sub()
