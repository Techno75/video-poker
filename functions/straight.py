def straight(card_list):
    list_of_correct_followin_value = []
    for i in range(len(card_list)-1):
        if card_list[i].get_value() - card_list[i + 1].get_value() == -1:
            list_of_correct_followin_value.append(True)

    if len(list_of_correct_followin_value) == 4:
        return True
    elif card_list[0].get_value() == 1 and card_list[1].get_value() == 10 and card_list[2].get_value() == 11 and card_list[3].get_value() == 12 and card_list[4].get_value() == 13:
       return True
    else:
     return False