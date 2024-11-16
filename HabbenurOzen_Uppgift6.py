def samla_information ():
  """
    Den här funktionen samlar in information om personer i form av ålder och kön.
    Funktionen låter användaren ange ålder och kön för flera personer och 
    användaren anger en -1 för att avsluta funktionen efter alla personers informationer samlas in.
    
    Returns:
        personer (list): En lista av dictionaries där varje dictionary innehåller
                         ålder och kön för en person, ex. {'ålder': 30, 'kön': 'M'}.
    """
  personer = []   # Jag skapar en lista för att lagra information om varje person
  while True :
    try:
       # Programmet frågar efter personens ålder, och låter användaren avsluta genom att ange -1
      ålder = int(input("Ange personens ålder (eller skriv -1 för att avsluta) : "))
      if ålder == -1 :
        break  # Programmet avslutar insamlingen om användaren anger -1
      
       # Programmet frågar efter personens kön och konverterar till versaler för enkel jämförelse
      kön = input("Ange personens kön (M för man, K för kvinna): ").strip().upper()
     
      # Programmet kontrollerar att kön är antingen 'M' (man) eller 'K' (kvinna)
      if kön not in ["M", "K"]:
        print ("Ogiltigt kön! Ange en 'M' för man eller 'K' för kvinna.")
        continue  # Programmet startar om loopen om ogiltigt kön angavs

       # Programmet lägger till personens ålder och kön som ett dictionary i listan
      personer.append({'ålder' : ålder, 'kön': kön})

    except ValueError:
          # Programmet hanterar fall där inmatningen för ålder inte är ett heltal
      print("Ogiltigt ålder. Vänligen ange ett heltal.")

  return personer

def beräkna_genomsnittsålder(personer):
    """
    Den här funktionen beräknar genomsnittsåldern för män respektive kvinnor i en grupp.
    
    Returns:
        tuple: Två värden, genomsnittlig ålder för män respektive kvinnor.
               (genomsnitt_ålder_män, genomsnitt_ålder_kvinnor)
    """
    # Progrsmmet filtrerar ut åldrarna för alla män i listan
    män = [person['ålder'] for person in personer if person['kön'] == 'M']
    kvinnor = [person['ålder'] for person in personer if person['kön'] == 'K']

     # Programmet filtrerar ut åldrarna för alla kvinnor i listan
 
   # Programmet beräknar genomsnittsåldern för män och kvinnor, men endast om listan inte är tom
    genomsnitt_ålder_män = sum(män) / len(män) if män else 0
    genomsnitt_ålder_kvinnor = sum(kvinnor) / len(kvinnor) if kvinnor else 0

    return genomsnitt_ålder_män, genomsnitt_ålder_kvinnor

def main():
   """
    Den här funktionen är Huvudfunktion för programmet. Funktionen samlar in information om flera personer,
    beräknar genomsnittsålder för män respektive kvinnor och presenterar resultatet.
    """
    # Programmet samlar in ålder och kön för varje person
personer = samla_information()

    # Programmet beräknar genomsnittsåldern för män och kvinnor
genomsnitt_ålder_kvinnor, genomsnitt_ålder_män = beräkna_genomsnittsålder(personer)

   # Programmet presenterar resultaten för användaren
print("\nResultat:")

  # Om det finns åldersdata för kvinnor, visar programmet genomsnittsåldern för kvinnor annars skriver ut Ingen data osv. 
if genomsnitt_ålder_kvinnor > 0 :
    print(f"Genomsnittålder för kvinnor är : {genomsnitt_ålder_kvinnor: .2f} år.")
else:
    print("Ingen data för kvinnor")

   # Om det finns åldersdata för män, visar programmet genomsnittsåldern för män annars skriver ut Ingen data osv.
if genomsnitt_ålder_män > 0 :
    print(f"Genomsnittålder för män är : {genomsnitt_ålder_män: .2f} år.")
else:
    print("Ingen data för män")

# Kör programmet
main()
