from functions.result import *
import random
from models.card import Card


def game(bet_value, player):
    color_list = ["Trèfle", "Coeur", "Pique", "Carrau"]
    value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    deck = []

    for value in value_list:
        for color in color_list:
            new_card = Card(value, color)
            deck.append(new_card)

    selected_cards = random.sample(deck, 5)

    print("Vous avez tiré : \n")

    for selected_card in selected_cards:
        player.add_card(selected_card)
        deck.remove(selected_card)
        print(selected_card.get_name())

    final_card_list = []

    for card_tmp in player.get_card_list():
        choice = input("\nVoulez vous garder : " + card_tmp.get_name() + " | oui/non ")
        if choice == "oui":
            final_card_list.append(card_tmp)
            print("ok, la carte est conservé")
        elif choice == "non":
            new_selected_card = random.sample(deck, 1)
            final_card_list.append(new_selected_card[0])
            deck.remove(new_selected_card[0])
            print("vous avez tiré :" + new_selected_card[0].get_name())
        else:
            final_card_list.append(card_tmp)
            print("Veleur incorrecte, la carte est conservé par défaut")

    player.update_all_cards(final_card_list)

    print("_______________________________________\n")
    print("Votre tirage final est : \n")

    for card_to_dispaly in player.get_card_list():
        print(card_to_dispaly.get_name())

    result(bet_value, player)
