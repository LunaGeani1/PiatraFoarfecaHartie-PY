import random

scorJucator=0
scorCalculator=0

#Alegerea jucatorului
def get_alegere_jucator():

    while True:
       alegere_jucator = input("Piatra, Foarfeca, Hartie? \n")
       if alegere_jucator not in ("Piatra","Foarfeca","Hartie"):
          print("Raspund gresit!")
       else:
        return alegere_jucator





def get_alegere_calculator():
    alegere=["Piatra","Foarfeca","Hartie"]
    alegere_claculator=random.choice(alegere)
    return alegere_claculator


#Determinare castigator"""
def Joc(alegere_jucator,alegere_calculator):
    global scorJucator,scorCalculator

    if (alegere_calculator == alegere_jucator):
        print("Este egalitate!")
    elif (alegere_jucator == 'Piatra' and alegere_calculator =='Foarfeca'):
        print("Jucatorul a castigat")
        scorJucator +=1


    elif(alegere_jucator == 'Foarfeca' and alegere_calculator =='Hartie'):
        print("Jucatorul a castigat!")
        scorJucator += 1


    elif(alegere_jucator == 'Hartie' and alegere_calculator == 'Piatra'):
        print("Jucatorul a castigat!")
        scorJucator += 1


    else:
        print("Calculatorul a castigat!")
        scorCalculator += 1





"""Jocul principal"""
while True:
    alegere_jucator=get_alegere_jucator()
    if alegere_jucator not in ("Piatra","Foarfeca","Hartie"):
        break
    else:
      alegere_calculator=get_alegere_calculator()

    print(f"Ai ales {alegere_jucator}, calculatorul a ales {alegere_calculator}")
    Joc(alegere_jucator,alegere_calculator)

    print(f"Scorul tau este {scorJucator} si scorul Calculatorului este {scorCalculator}")
    #if scorCalculator == 5:
     #   print("Calculatorul a castigat!")
    #else:
     #   print("Jucatorul a castigat!")





    Continuam=input("Vrei sa mai joci? (d/n)\n")
    if Continuam != 'd':
        break
"""Daca raspunsul este 'n' se opreste jocul"""