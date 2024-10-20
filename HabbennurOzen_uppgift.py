#Vi ska beräkna ett pris som inklusing moms med den här programmet
def berakna_moms(pris):
    moms = 0.25 
    totaltPris = pris + (moms * pris)  
    return totaltPris
try:
     #Vi tar ett pris från användaren med ett fönster som skriven 
     #"Ange pris exklusing moms"
     pris = float(input("Ange pris exklusing moms : "))
     #Vi ska testa först att vad händer om man skriver negativt? 
     if pris < 0:
          print("Priset kan inte vara negativt")
     #Vi ska beräkna pris inklusing moms via den här metoden
     #Om man skriver positivt, programmet ska beräkna totalt priset
     else:
          totaltPris= berakna_moms(pris)
          print("Totalt priset är :", totaltPris )
except ValueError:
    # Om användaren inte angav ett giltigt tal, programmet ska fånga felet
    print("Fel: Ange ett giltigt tal för pris exklusing moms.")

