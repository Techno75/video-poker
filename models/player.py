class Player:
    def __init__(self, name, money, card_list):
        self.name = name
        self.money = money
        self.card_list = card_list

    def get_name(self):
     return self.name

    def get_money(self):
     return self.money

    def get_card_list(self):
        return self.card_list

    def update_all_cards(self, new_card_list):
        self.card_list = new_card_list

    def add_card(self, card):
        self.card_list.append(card)

    def remove_card(self, card):
        self.card_list.remove(card)

    def reset_cards(self):
        self.card_list = []

    def win_money(self, value):
        self.money = self.money + value

    def loose_money(self, value):
        self.money = self.money - value

    def sort_card_by_value(self):
        self.card_list = sorted(self.card_list, key=lambda card: card.value)
        return  self.card_list