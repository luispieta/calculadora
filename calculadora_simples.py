escolha = ''

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def potenciar(num1, num2):
    return num1 ** num2

def restante(num1, num2):
    return num1 % num2

def inteiro(num1, num2):
    return num1 // num2

while escolha.lower() != 'sair':
    print('====MENU====')
    print('Digite o que deseja fazer \n Conta \n Sair')
    escolha = input('')

    def calculos():
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('===Parâmetros=== \n Soma (+) \n Subtração (-) \n Multiplicação (*) \n Divisão (/) \n Potência (**) \n Resto (%) \n Inteiro (//)')
        
        parametros = input('Digite um parâmetro: ')

        if parametros == '+':
            resultado1 = somar(num1, num2)
            print(resultado1)

        if parametros == '-':
            resultado2 = subtrair(num1, num2)
            print(resultado2)

        if parametros == '*':
            resultado3 = multiplicar(num1, num2)
            print(resultado3)

        if parametros == '/':
            resultado4 = dividir(num1, num2)
            print(resultado4)

        if parametros == '**':
            resultado5 = potenciar(num1, num2)
            print(resultado5)

        if parametros == '%':
            resultado6 = restante(num1, num2)
            print(resultado6)

        if parametros == '//':
            resultado7 = inteiro(num1, num2)
            print(resultado7)

    if escolha.lower() == 'conta':
        calculos()

print('Obrigado!')
