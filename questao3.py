def conversao(a, b):
    hora = a % 12
    minute = b
    if minute < 10:
        minute = '0' + str(minute)
    mostra_hora(f"{hora}:{minute} {padrao}")

def mostra_hora(qualquer_coisa):
    print(qualquer_coisa)
    
def lin():
    print('-' * 30)
    
lin()
print('Conversão de 24HRS para 12HRS')
lin()
while True:
     
    hora = int(input('Digite a hora(24hrs): '))
    
    if hora > 0 and hora < 12 or hora == 24:
        padrao = 'A.M'
    elif hora >= 12 and hora < 24:
        padrao = 'P.M'
    else: 
        print('Horario inválido! BURRO!')
        break
    
    minutos = int(input('Digite os minutos :'))
    conversao(hora,minutos)
