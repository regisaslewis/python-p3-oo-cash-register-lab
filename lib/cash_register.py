#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_purchase = 0
    
    def get_discount(self):
        return self._discount
    
    def set_discount(self, discount):
        if (type(discount) == int) and (0 <= discount <= 100):
            self._discount = discount
        else:
            print("Wrong-o dongo")

    discount = property(get_discount, set_discount)

    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        self.last_purchase = price * quantity
        for item in range(quantity):
          self.items.append(title)
    
    def apply_discount(self):
        if self.discount > 0:
          self.total = int(self.total - (self.total * (self.discount / 100)))
          print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_purchase

x = CashRegister()
x.add_item("eggs", 1.99)
x.add_item("tomato", 1.76)
print(x.items)