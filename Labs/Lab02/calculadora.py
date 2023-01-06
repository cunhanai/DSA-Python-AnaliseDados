"""LAB02 - Calculadora

Construa uma calculadora em Puthon com as funcoes soma, subtracao, multiplicacao e divisao
"""

# iniciando calculadora
print('------------------<CALCULADORA>------------------')

condicao = True
while condicao:
    opcao = int(input('Selecione a operacao desejada\n' +
                    '1 - soma\n' +
                    '2 - subtracao\n' +
                    '3 - multiplicacao\n' +
                    '4 - divisao\n' +
                    'Pressione qualquer outro numero para sair\n\n'))
    
    if opcao > 4 or opcao < 1:
        print('saindo')
        break
    
    n1 = float(input('\nPrimeiro numero: '))
    n2 = float(input('\nSegundo numero: '))
    print()
    
    if opcao == 1:
        print(n1, ' + ', n2, ' = ', (n1+n2))
    elif opcao == 2:
        print(n1, ' - ', n2, ' = ', (n1-n2))
    elif opcao == 3:
        print(n1, ' * ', n2, ' = ', (n1*n2))
    elif opcao == 4:
        print(n1, ' / ', n2, ' = ', (n1/n2))
    else:
        break
    
    print()