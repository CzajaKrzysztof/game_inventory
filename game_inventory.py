
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory.'''
    total_items = 0
    print("Inventory:")
    for i in inventory:
      total_items += inventory[i]
      print("{0} {1}".format(inventory[i], i))
    
    print("Total number of items: {0}". format(total_items))
    


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    pass


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

    pass


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''

    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inv)
