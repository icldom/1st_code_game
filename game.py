print("Rock...")
print("Paper...")
print("Scissors...")
rock = rockk
Dominik = input ("Dominik, make your move: ").lower()
print("***NO CHEATING !!!***\n" * 20)
Viliam = input ("Viliam, make your move: ").lower()

if Dominik == Viliam:
    print("It is bloody tie!")
elif Dominik == "rock":
    if Viliam == "paper":
        print("Viliam WINS !")
    elif Viliam == "scissors":
        print("Dominik WINS !")
elif Dominik == "paper":
    if Viliam == "rock":
        print("Dominik WINS !")
    elif Viliam == "scissors":
        print("Viliam 2 WINS !")
elif Dominik == "scissors":
    if Viliam == "rock":
        print("Viliam WINS !")
    elif Viliam == "paper":
        print("Dominik WINS !")
else:
    print("Something went wrong !")


