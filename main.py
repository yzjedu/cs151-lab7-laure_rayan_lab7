# Programmers:
# Course:  CS151, Dr. Zee
# Due Date:
# Programming Assignment:  Lab 07
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program



def input_dimension():
    dimension = input('What is the dimension of the floor in feet?')
    return dimension

def input_type():
    floor_type = input('What flooring type would you like for this room? The options are: \n\t1. Hardwood \n\t2.Carpet \n\t3. Tile')
    if floor_type == 'hardwood':
        floor_type = 1.39
    elif floor_type == 'carpet':
        floor_type = 3.99
    elif floor_type == 'tile':
        floor_type = 4.99
    return floor_type

def calc_cost (length, width, floor_type):
    room_cost = length * width * floor_type
    return room_cost

def main():
    total_cost = 0
    num_rooms = 0
    while num_rooms <= 5:
        length = input_dimension()
        width = input_dimension()
        floor_type = input_type()
        room_cost = calc_cost (length, width, floor_type)
        print(room_cost)
        total_cost += room_cost
        num_rooms += 1
    print(total_cost)

main()


