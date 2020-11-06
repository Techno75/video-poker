from functions.full import *
from functions.flush import *
from functions.pair import *
from functions.quads import *
from functions.royalstraight import *
from functions.straight import *
from functions.trips import *
from functions.twopairs import *


def result(bet_value, player):
    player.loose_money(bet_value)
    print("_________________________________________________")
    if royal_straight(player.sort_card_by_value()) == True and flush(player.sort_card_by_value()) == True:
        gain = bet_value * 250
        player.win_money(gain)
        print("Félicitation vous avez une Quinte Flush Royale!! vous remportez " + str(gain) + " €")
    elif flush(player.sort_card_by_value()) == True and straight(player.sort_card_by_value()) == True:
        gain = bet_value * 50
        player.win_money(gain)
        print("Félicitation vous avez une Quinte Flush !! vous remportez " + str(gain) + " €")
    elif quads(player.sort_card_by_value()) == True:
        gain = bet_value * 25
        player.win_money(gain)
        print("Félicitation vous avez un Carré !! vous remportez " + str(gain) + " €")
    elif full(player.sort_card_by_value()) == True:
        gain = bet_value * 9
        player.win_money(gain)
        print("Félicitation vous avez un full !! vous remportez " + str(gain) + " €")
    elif flush(player.sort_card_by_value()) == True:
        gain = bet_value * 6
        player.win_money(gain)
        print("Félicitation vous avez une couleur !! vous remportez " + str(gain) + " €")
    elif straight(player.sort_card_by_value()) == True:
        gain = bet_value * 4
        player.win_money(gain)
        print("Félicitation vous avez une suite !! vous remportez " + str(gain) + " €")
    elif trips(player.sort_card_by_value()) == True:
        gain = bet_value * 3
        player.win_money(gain)
        print("Félicitation vous avez un brelan !! vous remportez " + str(gain) + " €")
    elif two_pairs(player.sort_card_by_value()) == True:
        gain = bet_value * 2
        player.win_money(gain)
        print("Félicitation vous avez deux paires !! vous remportez " + str(gain) + " €")
    elif pair(player.sort_card_by_value()) == True:
        player.win_money(bet_value)
        print("Vous avez une paire !! vous remportez " + str(bet_value) + " €")
    else:
        print("Dommage !! vous perdez " + str(bet_value) + " €")

    player.reset_cards()
    print("Vous avez un crédit de " + str(player.get_money()) + " €")
    print("_________________________________________________")
