


def diference(lun,mar,mer,jeu,ven,sam,dim):
    all_day = {'Lundi':lun,'Mardi':mar,'Mercredi':mer,'Jeudi':jeu,
               'Vendredi':ven,'Samedi':sam,'Dimanche':dim}
    meilleur = max(all_day, key=all_day.get)
    pire = min(all_day, key=all_day.get)
    print('Le meilleur jour est :',meilleur)
    print(f'Le pire jour est :{pire}')
    return all_day

def some(vl):
    info = int(input(vl))
    return info



lun = 0
mar = 0
mer = 0
jeu = 0
ven = 0
sam = 0
dim = 0



lunn = True
while lunn:
    cant = some('Prix Lundi\n 0 pour change de jour')
    if cant == 0:
        lunn =False
    lun += cant
    pun = lun * 1 / 100
    print(f'total Lundi est: {lun}','et le pourcentage est: ',pun)


"""lunn = True
while lunn:
    cant = some('Prix Mardi\n 0 pour change de jour')
    if cant == 0:
        lunn = False
    mar += cant
    pun = mar * 1 / 100
    print(f'total Mardi est: {mar}','et le pourcentage est: ',pun)



lunn = True
while lunn:
    cant = some('Prix Mercredi\n 0 pour change de jour')
    if cant == 0:
        lunn = False
    mer += cant
    pun = mer * 1 / 100
    print(f'total Mercredi est: {mer}','et le pourcentage est: ',pun)


lunn = True
while lunn:
    cant = some('Prix Jeudi\n 0 pour change de jour')
    if cant == 0:
        lunn = False
    jeu += cant
    pun = jeu * 1 / 100
    print(f'total Jeudi est: {jeu}','et le pourcentage est: ',pun)



lunn = True
while lunn:
    cant = some('Prix Vendredi\n 0 pour change de jour')
    if cant == 0:
        lunn = False
    ven += cant
    pun = ven * 1 / 100
    print(f'total Vendredi est: {ven}','et le pourcentage est: ',pun)



lunn = True
while lunn:
    cant = some('Prix Samedi\n 0 pour change de jour')
    if cant == 0:
        lunn = False
    sam += cant
    pun = sam * 1 / 100
    print(f'total Samedi est: {sam}','et le pourcentage est: ',pun)



lunn = True
while lunn:
    cant = some('Prix Dimanche\n 0 pour voir le resultat de toute la semaine')
    if cant == 0:
        lunn = False
    dim += cant
    pun = dim * 1 / 100
    print(f'total Dimanche est: {dim}','et le pourcentage est: ',pun)
"""



print(diference(lun,mar,mer,jeu,ven,sam,dim))







