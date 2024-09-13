# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Vending machine class object to handle transaction cases.

class ValueError(Exception):
    """
    Exception to allow code to proceed in instances of insufficient items or funds.
    """
    pass


class VendingMachine:
    """
    Represents a vending machine with two public data members.
    Data member 1: num_items = number of items in vending machine
    Data member 2: item_price = price of item
    """

    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        """
        Method to purchase item.
        :param req_items (int): requested number of items.
        :param money (int): user's money value for payment of requested items.
        :return (int) remaining money to user.
        """
        # Successful transaction:
        if req_items <= self.num_items and money >= (self.item_price * req_items):
            self.num_items -= req_items
            return money - (self.item_price * req_items)

        # Request cannot be met:
        elif req_items > self.num_items:
            raise ValueError("Not enough items in the machine")

        # Insufficient payment from user:
        elif req_items <= self.num_items and money < (self.item_price * req_items):
            raise ValueError("Not enough coins")


if __name__ == '__main__':
    sodaPop = VendingMachine(10,2)
    trans1 = sodaPop.buy(1, 5)
    print(trans1)
    
    # Error test1 (insufficient product)
    # trans2 = sodaPop.buy(10, 100)
    # print(trans2)
    trans3 = sodaPop.buy(7, 100)
    print(trans3)

    # Error test2 (insuffient funds)
    # trans4 = sodaPop.buy(2,3)
    # print(trans4)



