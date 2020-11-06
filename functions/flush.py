def flush(card_list):
    hearts = []
    clubs = []
    diamonds = []
    spades = []

    for card in card_list:
        if card.color == "Trèfle":
            clubs.append(card)
        elif card.color == "Coeur":
            hearts.append(card)
        elif card.color == "Carrau":
            diamonds.append(card)
        elif card.color == "Pique":
            spades.append(card)

    if len(hearts) == 5:
        return True
    elif len(clubs) == 5:
        return True
    elif len(diamonds) == 5:
        return True
    elif len(spades) == 5:
        return True
    else:
        return False