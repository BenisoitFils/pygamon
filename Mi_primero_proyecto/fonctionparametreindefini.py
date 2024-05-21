def mul(*args):
# le resulta est egal a 1 parceque tout les nombre multiplie par 0 = 0
    resulta = 1
    for valor in args:
        resulta *= valor
    return resulta
print(mul(2,4,6,8))
