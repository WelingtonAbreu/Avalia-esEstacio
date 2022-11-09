def area(a, b, c):
    area = ((a + b) * c)/2
    print (f'A area do trapézio é: {area}')

basemaior = int(input('Digite o valor da base maior: '))
basemenor = int(input('Digite o valor da base menor: '))
altura = int(input('Digite o valor da altura: '))

area(basemaior,basemenor,altura)
