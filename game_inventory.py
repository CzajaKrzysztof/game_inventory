
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.

def get_total_items_count(inventory):
    """Caounts total number of items in inventory and terurn it as int."""
    total_items = 0
    for i in inventory:
      total_items += inventory[i]
    
    return total_items


def display_inventory(inventory):
    '''Display the inventory.'''
    print("Inventory:")
    for i in inventory:
      print("{0} {1}".format(inventory[i], i))
    
    print("Total number of items: {0}". format(get_total_items_count(inventory)))    


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for i in added_items:
      if i in inventory:
        inventory[i] +=1
      elif i not in inventory:
        inventory[i] = 1
    return inventory  

def get_max_key_length(inventory_keys):
    """Determinates longest key from inventory_keys and return in as int"""
    max_key_length = 0
    for i in inventory_keys:
      if len(i) > max_key_length:
        max_key_length = len(i)
    
    return max_key_length


def get_max_value_length(inventory_values):
    """Determinates longest value from inventory_values and return in as int"""
    max_values_length = 0
    for i in inventory_values:
      if len(str(i)) > max_values_length:
        max_values_length = len(str(i))
    
    return max_values_length


def get_sorted_inventory(inventory, order):
    """Sorts inventory by given order. Return ordered list of tuples."""
    if order == "count,asc":
      inventory_sorted = sorted(list(inventory.items()), key=lambda item: item[1])
    elif order == "count,desc":
      inventory_sorted = list(reversed(sorted(list(inventory.items()), key=lambda item: item[1])))
    elif order == None:
      inventory_sorted = list(inventory.items())
      
    return inventory_sorted


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified.

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    max_key_length = get_max_key_length(inventory.keys())
    max_value_length = get_max_value_length(inventory.values())
    sorted_inventory = get_sorted_inventory(inventory, order)

    print("Inventory:\n")
    print("{0:>{width_c}}{1:>{width_i}}".format("Count", "item name", width_c = max_value_length + 4, width_i = max_key_length + 3))
    print("-" * (max_key_length + max_value_length + 7))
    for i in sorted_inventory:
      print("{0:>{width_c}}{1:>{width_i}}".format(i[1], i[0], width_c = max_value_length + 4, width_i = max_key_length + 3))
    print("-" * (max_key_length + max_value_length + 7))
    print("Total number of items: {0}".format(get_total_items_count(inventory)))


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    with open(filename, "r") as import_file:
      imported_items = import_file.read().split(",")

    inventory = add_to_inventory(inventory, imported_items)
    print_table(inventory, "count,desc")


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass


#print("Step 1")
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#display_inventory(inv)

#print("\n\nStep 2")
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
#display_inventory(inv)

#print("\n\nStep 3")
#print_table(inv,"count,desc")

#print("\n\nStep 4")
import_inventory(inv, "test_inventory.csv")
