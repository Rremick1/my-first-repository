""" Grocery List
    Rachel Remick
    The purpose of this program is to create an organized user clairified grocery list.
    9/27/25
"""
from User import UserList
from groceries import Groceries 

def main():
    user_list = UserList()
    user_name = input("Enter your name: ")
    user_list.add_user(user_name)

    groceries = Groceries()
    grocery_item = input("Enter a grocery item: ")
    grocery_quantity = int(input("Enter the quantity: "))
    groceries.add_item(grocery_item, grocery_quantity)




if __name__ == "__main__":
    main()