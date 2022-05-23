import time
def truncate(n, decimals = 0):
    multiplier = 10 ** decimals 
    return int(n * multiplier) / multiplier
print()
start=int(input("Pour confirmer le lancement du chronometre taper 1 et appuyer sur \"Enter\"(un compte à rebour de 5s se lancera) : "))
while start==1:
    print("Le chronomètre va commecer dans :")
    for k in range (5,0,-1):
        print(k,"s")
        time.sleep(1)
    t1=time.time()
    print("Début du chronomètre.")
    print()
    print()
    stop=int(input("Pour arreter le chronometre entrer un chiffre entre 0 et 8, pour enregistrer un tour entrer le chiffre 9 : "))
    print()
    nbtour=0
    while stop==9:                                                          #système de tours
        tour=time.time()
        tour=tour-t1
        tourS=truncate(tour,4)
        tourmin=truncate(tourS/60,2)
        print("Tour n°",nbtour+1,":",tourS,"s ou",tourmin,"min.")
        print()
        print()
        stop=int(input("Pour arreter le chronometre entrer un chiffre entre 0 et 8, pour enregistrer un nouveau tour entrer le chiffre 9 : "))
        print()
        nbtour=nbtour+1                                            #tenter de mettre un système permêtant d'enregister les tours sur un doc
    if stop>=0 or stop <=8:
        t2=time.time()
        print("Arret du chronomètre...")
    t3=t2-t1
    t3s=truncate(t3,4)
    print()
    print()
    print("Temps d'execution du chronomètre en secondes :",t3s,"s.")
    t3min=truncate((t3s/60),2)
    print("Temps d'execution du chronomètre en minutes :",t3min,"min.")
    print()
    start=int(input("Voulez-vous lancer un nouveau chronometre ? (1.Oui; 2.Non) : "))
    t1=0
    t2=0
    t3=0
print()
print("Fin du programme.")