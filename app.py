from models.player import Player
from functions.game import *


def main():
    print("\n_________________________________________________")
    print('\nBienvenu sur le jeu VIDEO POKER')
    print("\n_________________________________________________")
    name = input("\nQuel est votre nom ? ")
    print("\n_________________________________________________")
    money = int(input("\nBonjour " + name + ". Combien de crédit voulez-vous acheter ? "))
    print("\n_________________________________________________")
    print("\nTrès bien, commençons la partie. Bonne Chance " + name + "!!")
    print("\n_________________________________________________")

    player = Player(name, money, [])

    while player.get_money() > 0:
        bet_value = int(input("\nCombien Voulez-vous miser ? "))
        print("\n_________________________________________________")
        if bet_value <= player.get_money():
            game(bet_value, player)
        else:
            print("\nJe suis désolé mais vous n'avez pas assez de crédit ")
            print("\n_________________________________________________")

    if player.get_money() < 1:
        print("\nJe suis désolé mais vous avez perdu tout vos crédits.\nVous aurez plus de chance la prochaine fois.")
        print("\n_________________________________________________")
        still_playing = input("\nVoulez-vous recommencer la partie ? oui/non ")
        if still_playing == "oui":
            main()
        else:
            print("\n_________________________________________________")
            print("Au revoir " + player.get_name())


main()