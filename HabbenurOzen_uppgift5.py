# Program: Ett program som simulerar kast med två tärningar.
# Beskrivning: Detta program simulerar kast med två tärningar.
# Programmeringssteg:
# 1. Jag använder funktionen ”random” för att randomisera tal.
# 2. Jag skapar en funktion som simulerar kastet och returnerar värdena för två tärningar.
# 3. Programmet skriver ut resultaten för varje kast.

import random

def kasta_tarningar():
    """
    Funktion som simulerar kast med två tärningar.
    Returnerar ett tuple med resultaten från de två tärningarna.
    """
    # Jag skapar två slumpmässiga tal mellan 1 och 6 för att simulera kast med två tärningar
    tarning1 = random.randint(1, 6)
    tarning2 = random.randint(1, 6)
    
    # Programmet returnerar värdena för varje tärning
    return tarning1, tarning2,

# Jag anropar funktionen för att kasta tärningarna
tarning1, tarning2 = kasta_tarningar()

# Programmet skriver ut resultaten av kastet
print(f"Tärning 1: {tarning1}")
print(f"Tärning 2: {tarning2}")

# Utvärdering av programmet
# Programmet uppfyller sitt syfte genom att simulera kast med två tärningar och visa resultatet.
# Det använder funktionen `kasta_tarningar()` för att göra kastet.
# Användningen av random.randint()` eliminerar behovet av mer komplexa slumptalsgeneratorer, vilket gör programmet enkelt och effektivt.
# random.randint()` nämns inte i läroboken, men jag lärde mig den när jag sökte efter hur man simulerar tärningar på internet.
# Funktionen random.randint(a, b) genererar ett slumpmässigt heltal mellan a och b (inklusive båda värdena).
# Möjliga förbättringar kan inkludera att låta användaren bestämma antal kast, eller att implementera en funktion för att visa statistik
# över flera kast, t.ex. medelvärde, antal gånger varje siffra kommer upp, etc.
