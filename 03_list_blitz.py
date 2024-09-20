## Task 1: Create list with 4 elements and print
# Variable = inventory
print("")
inventory = ["keys","phone", "radio", "wallet"]
print("1. Current inventory:")
print(inventory)
print("")

## Task 2: Add element to end of list and print updated list
# New element = "camera"
inventory.append("camera")
print("2. A new item is now in your inventory! Updated inventory:")
print(inventory)
print("")

## Task 3: Remove element and print updated list
inventory.remove("radio")
print("3. You lost an item! Updated inventory: ")
print(inventory)
print("")

## Task 4: Modify element and print updated list
inventory[3] = "flashlight"
print("4. One of your items have been traded! Updated inventory:")
print(inventory)
print("")

## Task 5: Append multiple elements to list and print updated list
inventory.append("radio")
inventory.append("camera")
inventory.append("tools")
inventory.append("charger")
print("5. Looks like you got some items back and some new ones as well! Updated inventory: ")
print(inventory)
print("")

## Task 6: Delete element at specific index and print updated list
del inventory[0]
print("6. You lost an item again, but in a strange way this time. Updated inventory:")
print(inventory)
print("")

## Task 7: Create new variable equal to first 2 items of list and print new list
# Variable = new_inventory
new_inventory = ["keys", "phone"]
print("7. You have a new inventory! Here's the new items: ")
print(new_inventory)
print("")

## Task 8: Extend current list with new list
big_inventory = inventory + new_inventory
print("8. You have a grand inventory from both inventories! Updated list: ")
print(big_inventory)
print("")