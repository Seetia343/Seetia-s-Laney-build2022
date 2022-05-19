'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
checklist = []

# Define Functions
def create(item):
    # Create item code here
    checklist.append(f"[ ] {item}")

def read(index):
    # Read code here
    print( checklist[index] )
    

def update(index, item):
    # Update code here
    checklist[index] = f"[ ] {item}" 

def destroy(index):
    # Destroy code here -- you could also use list.pop(index)
    del checklist[index]

def mark_completed(index):
    # Add code here that marks an item as completed
    ''' Lets say that our checklist is (of strings) [hey, how, are, you, doing] and that our index is 2
        checklist[2] = "are"
        checklist[2][1] = "r"
    '''
    if "√" not in checklist[index]:
        checklist[index] = f'[√] {checklist[index]}'

        return print(f"{checklist[index]} was marked completed")
        
    else:
        
        return print(f"That item was marked completed already")

def list_all_items():
    # List all items code here
    for item in checklist:
        print(item)

def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = input("What would you like to add to the list: ")
        create(input_item)
        running = True

        return running

    elif function_code =="R" :
        input_item = input("Enter the index position you are trying to access in the list:")
        read(int(input_item))
        running = True
    
        return running
    
    elif function_code == "U" :
        input_index = input("Enter the index position you are trying to update in the list:")
        input_item = input("Enter the element you are trying to update to the list:")
        update(int(input_index), input_item)
        running = True

        return running 

    elif function_code == "D":
        input_index = input("Enter the index position of the element you want to delete:")
        destroy(int(input_index))
        running = True

        return running

    elif function_code =="L":
        list_all_items()
        running = True
    
        return running

    elif function_code =="Q":
        running = False

        return running
   
    elif function_code =="M":
        input_index = input("Enter the index position you are trying to mark complete:")
        mark_completed(int(input_index))
        running = True

        return running

running = True  

while running:
    selection = input(
           "Press C to add to list, R to Read from list, U to update list , D to delete from the list, L to displaylist,M for mark completed   and Q to quit: ").upper()
    running = select(selection)