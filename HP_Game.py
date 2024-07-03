import random

def shuffle_cards():
    HP_cards = [
        ("Harry Potter", 78), ("Dumbledore", 85), ("Hermione Granger ", 79), ("Voldermort", 84), ("Lily Potter", 75), ("James Potter", 77), ("Ron Weasley", 82), ("Draco Malfoy", 83),
        ("Rubeus Hagrid", 55), ("Severus Snape", 76), ("Tonks", 81), ("Minerva McGonagall ", 80),
        ("Pomona Sprout", 69), ("Filius Flitwick", 65), ("Dobby", 54), ("Luna Lovegood", 60),
        ("Lucius Malfoy", 74), ("Sirius Black", 73), ("Remus Lupin", 72), ("Peter Pettigrew", 59)
    ]
    random.shuffle(HP_cards)
    return HP_cards


def pass_out(cards):
    player1_cards = cards[:10]
    player2_cards = cards[10:20]
    return player1_cards, player2_cards

def display_cards(cards, show_power=False):
    for i, (pokemon, power) in enumerate(cards, start=1):
        if show_power:
            print(f"{i}. {pokemon} (Power: {power})")
        else:   
            print(f"{i}. {pokemon}")  
    return 

def choose_card(cards):
    while True:
        try:
            choice = int(input("\nChoose a card by number: "))      #error here
            card = cards[choice - 1]
            return card
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid card number.")


# def name():
#     player1 = input("Enter Player 1's  name: ")
#     player2= input("Enter Player 2's name: ")
#     # global(player1) = input("Enter Player 1's  name: ")
#     # global(player2)= input("Enter Player 2's name: ")
#     # global(player1)
#     # global(player2)
#     return player1 and player2

def game():

    # player1 = input("Enter Player 1's  name: ")
    # player2= input("Enter
    #  Player 2's name: ")
    cards = shuffle_cards()
    player1_cards, player2_cards = pass_out(cards)
    print(f"\n\n{player1}'s turn\n")
    display_cards(player1_cards)
    player1_card = choose_card(player1_cards)
    player1_cards.remove(player1_card)
    print(f"\n\n\n{player2}'s turn")
    display_cards(player2_cards)
    player2_card = choose_card(player2_cards)
    player2_cards.remove(player2_card)

    print("\nResults:")
    print(f"{player1} chose {player1_card[0]} and its power was {player1_card[1]}")
    print(f"{player2} chose {player2_card[0]} and its power was {player2_card[1]}")


    if player1_card[1] > player2_card[1]:
        print(f"\n\n{player1} wins!!!")  
        return 1
    elif player2_card[1] > player1_card[1]:
        print(f"\n\n{player2} wins the round!!!")
        return 2 




player1 = input("Enter Player 1's  name: ")
player2= input("Enter Player 2's name: ")

player11=0
player22=0
for i in range (3):
    num=game()
    num=int(num)
    if num==1:
        player11+=1
    if num==2:
        player22+=2

if player11>player22:
    print(f"\n\nThe Winner is player 1!!!" )

if player22>player11:
    print(f"\n\nThe Winner is player 2 !!! ")

else:
    print("\n\nThe game is tied!!!")
