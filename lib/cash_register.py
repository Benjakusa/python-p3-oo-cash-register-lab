#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []  # Store all transactions as (title, price, quantity)
    
    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        
        # Add to items list
        for _ in range(quantity):
            self.items.append(title)
        
        # Record transaction
        self.transactions.append((title, price, quantity))
        return self.total
    
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        if not self.transactions:
            return
        
        # Get the last transaction
        title, price, quantity = self.transactions.pop()
        
        # Subtract from total
        self.total -= price * quantity
        
        # Remove items from items list
        for _ in range(quantity):
            if title in self.items:
                self.items.remove(title)
        
        # If no items left, total should be 0.0
        if not self.items:
            self.total = 0.0