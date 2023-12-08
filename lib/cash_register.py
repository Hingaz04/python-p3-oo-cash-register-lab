#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item, price, quantity=1):

        pass

    def apply_discount(self):

        pass

    def void_last_transaction(self):

        pass
