print ('q - quadrado, t - triangulo, c - circulo')
figura = input ('Digite qual figura voce deseja calcular: ')

match figura:
    case 'q':
        lado = float (input ('digite o lado:'))
        quadrado = lado ** 2
        print ('O calculo de quadrado é ', (quadrado))
    case 't':
        base = float (input('digite a base'))
        altura = float (input('digite a altura'))
        calculo = (base * altura)/2
        print ('Area: {}'.format(calculo))
    case 'c':
        raio = float(input('raio:'))
        calculo = 3.14 * (raio**2)
        print ('Area: {}'.format(calculo))