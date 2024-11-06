# Programmers: Laure Patera and Rayan Haq
# Course:  CS151, Dr. Zee
# Due Date: 10/31/2024
# Programming Assignment:  Lab 07
# Problem Statement:  calculates cost to floor rooms of a house based on dimensions and floor type
# Data In: length, width, and floor type
# Data Out:  room_cost, total_cost
# Credits: based on instructions from read me file and example given on the board in class

# Purpose:  asks user to input a dimension
# Parameters: none
# Return: dimension as a float
def input_dimension():
    dimension = float(input('What is the dimension of the floor in feet?'))
    while dimension <= 0:
        dimension = float(input('What is the dimension of the floor in feet? Please input a valid number.'))
    return dimension

# Purpose:  asks user to input a type
# Parameters: none
# Return: floor type as a string
def input_type():
    floor_type = input('What flooring type would you like for this room? The options are: \n\t1. Hardwood $1.39/sqft \n\t2.Carpet $3.99/sqft \n\t3. Tile $4.99/sqft')
    floor_type.lower().strip()
    while floor_type != 'hardwood' or floor_type != 'carpet' or floor_type != 'tile':
        floor_type = input('What flooring type would you like for this room? The options are: \n\t1. Hardwood $1.39/sqft \n\t2.Carpet $3.99/sqft \n\t3. Tile $4.99/sqft')
    if floor_type == 'hardwood':
        floor_type = 1.39
    elif floor_type == 'carpet':
        floor_type = 3.99
    elif floor_type == 'tile':
        floor_type = 4.99
    return floor_type

# Purpose:  calculate the cost of flooring a room
# Parameters: length, width, floor_type
# Return: room_cost as a float,
def calc_cost (length, width, floor_type):
    room_cost = length * width * floor_type
    return room_cost


# Purpose:  main function
# Parameters: none
# Return: none
def main():
#Output purpose of the program
    print('Welcome! This program finds the cost of flooring rooms based on dimensions and floor type.')
#initialize variables
    total_cost = 0
    num_rooms = 0
#find room cost
    while num_rooms <= 5:
        length = input_dimension()
        width = input_dimension()
        floor_type = input_type()
        room_cost = calc_cost (length, width, floor_type)
        print(room_cost)
#give option to see cost of the room with a different flooring type
        option = input('Would you like to see the cost with a different floor type? y/n')
        option.lower().strip()
        while option != 'y' and option != 'n':
            option = input('Would you like to see the cost with a different floor type? y/n')
        if option == 'y':
            floor_type = input_type()
            room_cost = calc_cost(length, width, floor_type)
            print(room_cost)
        elif option == 'n':
            total_cost += room_cost
            num_rooms += 1
#output total cost to the user and end
    print(total_cost)
    print('Thank you for using the program!')

main()


