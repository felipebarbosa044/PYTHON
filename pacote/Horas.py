segundos = int(input("Digite segundos "))
minutos = 60
horas = 3600
dia = 86400
semana = 604800
mes = 2592000


print(f'Minutos: {(segundos // minutos) % minutos}')
print(f'Horas: {(segundos // horas) % 24}')
print(f'Dias: {(segundos // dia) % 7}')
print(f'Semanas: {(segundos // semana) % 30}')
print(f'Meses: {(segundos // mes) % 365}')

