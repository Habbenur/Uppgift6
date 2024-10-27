# Jag skapar ett Python-program som räknar antalet vokaler i en text.

# Steg 1: Jag ska be användaren om en textinmatning
text = input("Ange en text: ")
def veriferaTecken(text):
# Steg 2: Jag definierar variabler för vokaler och räknare
    vokaler = "aeiouAEIOU"  # Lista över vokaler, både små och stora bokstäver
    antal_vokaler = 0       # Variabel för att hålla räkningen på vokaler

# Steg 3: Programmet kommer att gå igenom varje tecken i texten
    for tecken in text:
    # Programmet kontrollerar om tecknet är en vokal
        if tecken in vokaler:
            antal_vokaler += 1  # Om tecknet är en vokal, ökar programmet räkningen
    return antal_vokaler
antalTecken = veriferaTecken(text)    
if antalTecken > 0:
     # Steg 4: Programmet skriver ut resultatet till användaren
    print(f"Antalet vokaler i texten är : {antalTecken}")
     # Steg 5: Om användaren skriver in en ogiltig text skriver programmet ut ett felmeddelande.
else:
    print("Fel: Ange en giltig text!")

#Kort utvärdering: 
# Programmet är av god nivå och fungerar för att hitta det totala antalet vokaler i texten som tas emot från användaren. 
# Användarens inmatning är begränsad till text. 
# Programmet ger en varning om ett numeriskt värde matas in, men programmet fortsätter inte automatiskt efter varningen. 
# Användaren måste köra programmet igen efter felmeddelandet. 
# Det finns inte heller någon längdbegränsning för den text som tas emot från användaren. 

