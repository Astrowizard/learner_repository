from random import randint

check = True
computerpoint = 0
personpoint = 0

while check == True:
    person = input("Rock, Paper, Scissors \n")
    person = person.lower()
    if person == "rock":
        personint = 0
    elif person == "paper":
        personint = 1
    elif person == "scissors":
        personint = 2
    else:
        print ("Choice not recognized")
    
    computer = randint(0,2)
    
    if computer == 0:
        print ("computer: rock")
    elif computer == 1:
        print ("computer: paper")
    elif computer == 2:
        print ("computer: scissors")
    
    if personint == computer:
        print ("Tie")
    elif (personint == 0 and computer == 1) or (personint == 1 and computer == 2) or (personint == 2 and computer == 0):
        print ("lose")
        computerpoint += 1
    else:
        print ("win")
        personpoint += 1
    print ("player: %s | computer: %s" % (personpoint,computerpoint))
    ask = input("Another? y/n\n")
    if ask[0].lower() == "n":
        check = False
