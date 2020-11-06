import pandas as pd
import random
from models.player import Player
from models.card import Card
from functions.full import *
from functions.flush import *
from functions.pair import *
from functions.quads import *
from functions.royalstraight import *
from functions.straight import *
from functions.trips import *
from functions.twopairs import *

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

    color_list = ["Trèfle", "Coeur", "Pique", "Carrau"]
    value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    player = Player(name, money, [])

    def result(bet_value):
        player.loose_money(bet_value)
        print("_________________________________________________")
        if royal_straight(player.sort_card_by_value()) == True and flush(player.sort_card_by_value()) == True:
            gain = bet_value * 250
            player.win_money(gain)
            print("Félicitation vous avez une Quinte Flush Royale!! vous remportez " + str(gain))
        elif flush(player.sort_card_by_value()) == True and straight(player.sort_card_by_value()) == True:
            gain = bet_value * 50
            player.win_money(gain)
            print("Félicitation vous avez une Quinte Flush !! vous remportez " + str(gain))
        elif quads(player.sort_card_by_value()) == True:
            gain = bet_value * 25
            player.win_money(gain)
            print("Félicitation vous avez un Carré !! vous remportez " + str(gain))
        elif full(player.sort_card_by_value()) == True:
            gain = bet_value * 9
            player.win_money(gain)
            print("Félicitation vous avez un full !! vous remportez " + str(gain))
        elif flush(player.sort_card_by_value()) == True:
            gain = bet_value * 6
            player.win_money(gain)
            print("Félicitation vous avez une couleur !! vous remportez " + str(gain))
        elif straight(player.sort_card_by_value()) == True:
            gain = bet_value * 4
            player.win_money(gain)
            print("Félicitation vous avez une suite !! vous remportez " + str(gain))
        elif trips(player.sort_card_by_value()) == True:
            gain = bet_value * 3
            player.win_money(gain)
            print("Félicitation vous avez un brelan !! vous remportez " + str(gain))
        elif two_pairs(player.sort_card_by_value()) == True:
            gain = bet_value * 2
            player.win_money(gain)
            print("Félicitation vous avez deux paires !! vous remportez " + str(gain))
        elif pair(player.sort_card_by_value()) == True:
            player.win_money(bet_value)
            print("Vous avez une paire !! vous remportez " + str(bet_value))
        else:
            print("Dommage !! vous perdez " + str(bet_value))

        player.reset_cards()
        print("Vous avez un crédit de " + str(player.get_money()))
        print("_________________________________________________")

    def game(bet_value):
        deck = []

        for value in value_list:
            for color in color_list:
                new_card = Card(value, color)
                deck.append(new_card)

        selected_cards = random.sample(deck, 5)

        print("Vous avez tiré : ")

        for selected_card in selected_cards:
            player.add_card(selected_card)
            deck.remove(selected_card)
            print(selected_card.get_name())

        for card_tmp in player.get_card_list():
            choice = input("\nVoulez vous garder : " + card_tmp.get_name() + " | oui/non ")
            if choice == "oui":
                print("ok, la carte est conservé")
            elif choice == "non":
                player.remove_card(card_tmp)
                new_selected_card = random.sample(deck, 1)
                print("vous avez tiré :" + new_selected_card[0].get_name())
                player.add_card(new_selected_card[0])
                deck.remove(new_selected_card[0])
            else:
                print("Veleur incorrecte, la carte est conservé par défaut")

        print("_______________________________________\n")
        print("\nVotre tirage final est : \n")

        for card_to_dispaly in player.get_card_list():
            print(card_to_dispaly.get_name())

        result(bet_value)

    while player.get_money() > 0:
        bet_value = int(input("\nCombien Voulez-vous miser ? "))
        print("\n_________________________________________________")
        if bet_value <= player.get_money():
            game(bet_value)
        else:
            print("Je suis désolé mais vous n'avez pas assez de crédit ")
            print("\n_________________________________________________")


    if player.get_money() < 1:
        print("\n_________________________________________________")
        print("\nJe suis désolé mais vous avez perdu tout vos crédits.\nVous aurez plus de chance la prochaine fois.")
        print("\n_________________________________________________")
        still_playing = input("\nVoulez-vous recommencer la partie ? oui/non ")
        if still_playing == "oui":
            money = int(input("\n Combien de crédit voulez-vous acheter? "))
            player.win_money(money)
            play()
        else:
            print("\n_________________________________________________")
            print("Au revoir " + player.get_name())

main()