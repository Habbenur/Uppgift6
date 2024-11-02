# Jag skapar ett program som utför "Binär Omvandling av Tre Heltal"
# Syfte av programmet är; Programmet tar emot tre heltal från användaren, konverterar varje tal till binär form och lagrar dem i en lista.
# Jag ska dokumentera i varje steg i koden för att förklara hur programmet fungerar.

# Steg 1: Programmet tar emot tre heltal från användaren och sparar dem i en lista
heltal = []
for i in range(1, 4):  # Loopar tre gånger för att ta emot tre tal
    try:
        # Programmet begärar ett heltal från användaren och konverterar till int
        tal = int(input(f"Skriv in heltal nummer {i}: "))
        # Programmet lägger till talet i listan 'heltal'
        heltal.append(tal)
    except ValueError:
        # Programmet hanterar fall där användaren inte anger ett heltal
        print("Fel: Ange ett giltigt heltal.")
        exit()

# Steg 2: Programmet omvandlar varje heltal till binär form och sparar i en ny lista
binar_lista = []
for tal in heltal:
    binar_tal = bin(tal)  # Programmet omvandlar talet till binär form med bin() formula
    binar_lista.append(binar_tal)  # Programmet lägger till binärt tal i listan

# Steg 3: Programmet skriver ut listan med de binära representationerna
print("Binära representationer:", binar_lista)

# --- Dokumentation av programmet ---

# Planering:
# 1. Programmet begär tre heltal från användaren.
# 2. Programmet kontrollerar om inmatningen är ett heltal. Om inte, visas ett felmeddelande.
# 3. Varje heltal omvandlas till binär form med bin() och sparas i en lista.
# 4. Listan med de binära talen skrivs ut.

# Utvärdering:
# Programmet är robust genom att hantera ogiltiga inmatningar med hjälp av try-except för att säkerställa att endast heltal tas emot.
# Det är enkelt att utöka programmet om fler heltal behövs.
# Genom att använda bin() för binär omvandling kan vi enkelt konvertera och hantera talen. Programmet är effektivt och användarvänligt.
