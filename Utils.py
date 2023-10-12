############################################
# Utils.py
# Utility functions
############################################

# getUserChoice()
# Displays a list of options, prompts for an option, and returns it
# Pass it a list of lists in format [["Letter","Display Text"]]
# Example: [["A","Option A"],["B","Option B"],["C","Option C"]]
# Returns selected letter
def getUserChoice(options):
    validInputs = ""
    for opt in options:
        validInputs += opt[0]
        print(opt[0], "-", opt[1])
    
    prompt = "Ce vrei să faci? [" + validInputs + "]: "
    choice = ""
    done = False

    while not done:
        choice = input(prompt).strip().upper()
        # If the user entered more than 1 character
        if len(choice) > 1:
            choice = choice[0]
        # Do we have 1 valid input?
        if len(choice) == 1 and choice in validInputs:
            done = True
    
    return choice


# inputYesNo()
# Displays a list of options, prompts for an option, and returns it
# Pass it a list in format [["Display Text","Display Text"]]
# Example: ["Accepți misiunea? (da/nu)", "Excelent! Vino cu noi și hai să salvăm lumea!"]
def inputYesNo(text):
    while True:
        # Display prompt
        x = input(text + " [da/nu]\n").strip().lower()      
        # Check response
        if x in ["da"]:
            return True
        elif x in ["nu"]:
            return False
        else:
            print("Nu am înțeles răspunsul tău. Te rog să răspunzi cu 'da' sau 'nu'.")


# inputNumber()
# Numeric input function
def inputNumber(prompt):
    while True:
        try:
            # Capturăm alegerea jucătorului
            alegere = int(input())

            # Verificăm validitatea alegerii
            if 1 <= alegere <= 3:
                return alegere
            else:
                print("Te rog să alegi o misiune dintre cele prezentate (1, 2 sau 3).")
        except ValueError:
            print("Te rog să introduci un număr corespunzător misiunii pe care vrei să o alegi.")
