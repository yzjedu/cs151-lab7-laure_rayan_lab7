# Programmers:
# Course:  CS151, Dr. Zee
# Due Date:
# Programming Assignment:  Lab 07
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program

HARDWOOD = 1.39
CARPET = 3.99
TILE = 4.99


def calc_room_area (room_width, room_length):
    floor_area = room_length * room_width
    return floor_area
def calc_room_floor_cost (floor_area, floor_type):
    floor_area * floor_type
