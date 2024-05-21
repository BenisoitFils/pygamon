"""def logvl(vl):
    info = input(vl)
    return info

usuario = input('usuario')
contra = input('pass')
help = input('tu color')
help1 = input('tu auto')
con_error = 0

vlu = ''
vlc = ''

print('usuario login')

while True:
    logu = logvl('utilisateur')
    if logu == usuario:
        break
    else:
        con_error += 1
        if con_error == 3:
            print('cuenta bloquiada')
            reinitia = logvl('tu color')
            reinitia1 = logvl('tu auto')

            if reinitia == help and reinitia1 == help1:
                print('tu usuario fue', usuario, 'y tu contraseña fue', contra,
                      'para modificar tu cuenta ingresa si, sino n')
                recuperar = logvl('')
                if recuperar == 'si':
                    n_usuario = logvl('nuevo usuario')
                    n_contra = logvl('nuevo contra')
                    print(n_usuario, n_contra)
            break
        print('wrong username')



while True:
    logc = logvl('contra')

    if logc == contra:
        print('connected successfully', con_error)
        break
    else:
        con_error += 1
        if con_error == 3:
            print('cuenta bloquiada')
            reinitia = logvl('tu color')
            reinitia1 = logvl('tu auto')

            if reinitia == help and reinitia1 == help1:
                print('tu usuario fue', usuario, 'y tu contraseña fue', contra,'para modificar tu cuenta ingresa si, sino n')
                recuperar = logvl('')
                if recuperar == 'si':
                    n_usuario = logvl('nuevo usuario')
                    n_contra = logvl('nuevo contra')
                    print(n_usuario, n_contra)

            break
        print('wrong password')"""




"""fruits = ["pomme", "banane", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

ma_liste = [10, 20, 30, 40, 50]

# Changer les valeurs aux indices 1 et 3
ma_liste[0:5] = [25, 45, 60, 100, 200]

print(ma_liste)

mon_dict = {'a': 10, 'b': 30, 'c': 15, 'd': 25}

# Trouver la clé associée à la plus grande valeur dans le dictionnaire
cle_max = max(mon_dict, key=mon_dict.get)

# Trouver la plus grande valeur elle-même
valeur_max = mon_dict[cle_max]

print(f"La clé avec la plus grande valeur est '{cle_max}' avec la valeur {valeur_max}.")




def diference(lun,mar,mer):
    all_day = {'lundi':lun,'mardi':mar,'mercredi':mer}
    meilleur = max(all_day, key=all_day.get)
    pire = min(all_day, key=all_day.get)
    print('Le meilleur jour est :',meilleur)
    print(f'Le pire jour est :{pire}')
    return all_day



lun = 0
mar = 0
mer = 0
jeu = 0
ven = 0
sam = 0
dim = 0
vent = 0



boucle = 3
while boucle != 0:
    boucle -=1
    cant = int(input('combien lun'))
    lun += cant


print(f'total lun est {lun}')


boucle = 3
while boucle != 0:
    boucle -=1
    cant = int(input('combien mar'))
    mar += cant


print(f'total mar est {mar}')



boucle = 3
while boucle != 0:
    boucle -=1
    cant = int(input('combien mer'))
    mer += cant
   

print(f'total mer est {mer}')




print(diference(lun,mar,mer))

"""

def chatbot(question):
    # Conversion de la question en minuscules pour faciliter la comparaison
    question = question.lower()

    # Logique de décision simple
    if "bonjour" in question:
        return "Bonjour! Comment puis-je vous aider aujourd'hui?"
    elif "météo" in question:
        return "Je suis un simple chatbot et je ne peux pas fournir la météo pour le moment."
    elif "python" in question:
        return "Python est un langage de programmation puissant et polyvalent."
    else:
        return "Je ne comprends pas bien. Pouvez-vous reformuler votre question?"

# Utilisation du chatbot
while True:
    user_input = input("Vous: ")
    if user_input.lower() == 'exit':
        print("Au revoir!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
