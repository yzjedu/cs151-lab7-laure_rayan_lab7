# Programmers:
# Course:  CS151, Dr. Zee
# Due Date:
# Programming Assignment:  Lab 07
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program


balance = 0
HARDWOOD = 1.39
CARPET = 3.99
TILE = 4.99

def calc_room_area (room_width, room_length):
    room_length = input('What is the length of the room in feet?')
    room_width = input('What is the width of the room in feet?')
    floor_area = room_length * room_width
    return floor_area

def calc_floor_type (floor_type):
    floor_type = input('Which floor type would you like for this room? The options are: \n\t1. Hardwood \n\t2.Carpet \n\t3. Tile')
    return floor_type

def calc_room_cost (floor_area, floor_type):
    cost = floor_area * floor_type
    return cost

def sum_cost (cost):
    balance = 0
    balance = balance + cost
    return balance


