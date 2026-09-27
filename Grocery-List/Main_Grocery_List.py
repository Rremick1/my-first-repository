""" Grocery List
    Rachel Remick
    The purpose of this program is to create an organized user clairified grocery list.
    9/27/25
"""


from glist import Glist

def main():

    answer: str =input("Would you like to add to the list (yes/no)?: ")
    groceries = Glist()
    while answer == "yes" or answer == "Yes":
        user_name = input("Enter your name: ")
        grocery_item = input("Enter a grocery item: ")
        grocery_quantity = int(input("Enter the quantity: "))
        groceries.add_item(user_name, grocery_item, grocery_quantity)
        for name, item, quantity in groceries.items:
            print(f" {name} has added {item}: {quantity} to the list")
        answer = input("add another item (yes/no)?: ")

    print("Your grocery list:")
    for name, item, quantity in groceries.items:
        print(f" {name}: {item}: {quantity} to the list")



if __name__ == "__main__":
    main()