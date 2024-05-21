
def fundo(deuda,gastos):
    return deuda + gastos
print('Hola Paulina como esta?')
sueldo = 500
deuda = 200
gastos = 150

gasto_total = fundo(deuda,gastos)
print(f'los gastos de este mes son {gasto_total}')
#print(f'los gastos de este mes son {fundo(deuda,gastos)}')
print(f'los dinero guarden son {sueldo-gasto_total}')
if deuda + gastos < sueldo:
    print(f'cliente puede ahorrar  {sueldo-gasto_total} $')
else:
    print('el cliente no puede ahorrar')







