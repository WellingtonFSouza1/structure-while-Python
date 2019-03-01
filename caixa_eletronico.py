print('-' * 8, 'BEM VINDO AO BANCO FELIX', '-' * 8)

while True:
    saque = int(input('Qual é o valor do saque?'))
    total = saque
    ced = 50
    totced = 0

    #Contando as cédulas.
    while True:
            if total >= ced:
                total -= ced
                totced += 1
            else:
                if totced > 0:
                    print(f'       {totced} cedulas de {ced}')
                if ced == 50:
                    ced = 20
                    totced = 0
                elif ced == 20:
                    ced = 10
                    totced = 0
                elif ced == 10:
                    ced = 1
                    totced = 0
                if total == 0:
                    break      #Operação finaliza quando chega ao 0

    print('Operação realizada com sucesso!.')
    print('-' * 42)
    print('Você quer realizar outro saque? ')
    decisao = str(input(' ----------[S||N]-----------\n             ')).strip()[0].upper()
    print('-' * 42)
    
    while decisao not in 'SN':     #analizando se a opçao e S OU N.
        print('OPÇÃO INVALIDA!.')
        decisao = str(input('[S||N]')).strip()[0].upper()
        print('-' * 42)
    if decisao == 'N':
        break
#Fim do código.  
print('Operação finalizada com sucesso!.')
print('-' * 4