def quads(card_list):
    value_list = []
    for val in card_list:
        value_list.append(str(val.value))

    filtered_value_list = []
    for value in set(value_list):
        filtered_value_list.append(value_list.count(value))

    sorted_list = sorted(filtered_value_list, reverse=True)[:1]
    if sorted_list[0] == 4:
        return True
    else:
        return False
