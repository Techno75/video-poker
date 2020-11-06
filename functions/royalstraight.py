def royal_straight(card_list):
    if card_list[0].get_value() == 1 and card_list[1].get_value() == 10 and card_list[2].get_value() == 11 and card_list[3].get_value() == 12 and card_list[4].get_value() == 13:
        return True
    else:
        return False
