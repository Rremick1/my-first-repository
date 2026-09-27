
""" Grocery List
    Rachel Remick
    The purpose of this class is to represent the grocery list itself.
    9/27/25
"""
class Glist:
    def __init__(self):
        self.items = []

    def add_item(self, name, items, quantity):
        self.items.append((name, items, quantity))


    

    