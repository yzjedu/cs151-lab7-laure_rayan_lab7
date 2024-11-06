# Algorithm

- **name: input_dimension**
- purpose: ask user to input a dimension
- params: none
- return: dimension
- algorithm:
  1. set the variable dimension equal to user input, with the question, "What is the dimension of the floor in feet?"
  2. while dimension is less than or equal to 0
     1. set the variable dimension equal to user input, with the question, "What is the dimension of the floor in feet? Please input a valid number."
  3. return dimension


- **name: input_type**
- purpose: asks user to input a floor type
- params: none
- return: floor_type
- algorithm:
    1. set the variable floor_type equal to user input, with the question, "What flooring type would you like for this room? The options are: 1. Hardwood 1.39/sqft, 2.Carpet 3.99/sqft, 3. Tile 4.99/sqft"
  2. convert floor_type to lowercase and strip any whitespace
  3. While floor_type does not equal hardwood, carpet, or tile,
     1. set the variable floor_type equal to user input, with the question, "What flooring type would you like for this room? The options are: 1. Hardwood 1.39/sqft, 2.Carpet 3.99/sqft, 3. Tile 4.99/sqft"
  4. if floor_type equals hardwood
     1. set floor_type equal to 1.39
  5. otherwise if floor_type equals carpet
     1. set floor_type equal to 3.99
  6. otherwise if floor_type equals tile
     1. set floor_type equal to 4.99
  7. return floor_type


- **name: calc_cost**
- purpose: calculate the cost of flooring a room
- params: length, width, floor_type
- return: room_cost
- algorithm:
    1. set variable room_cost equal to length * width * floor_cost
  2. return room_cost


- **name: main**
- purpose: main function
- params: none
- return: none
- algorithm:
    1. output to the user, "Welcome! This program finds the cost of flooring rooms based on dimensions and floor type."
  2. set variable total_cost equal to 0
  3. set variable num_rooms equal to 0
  4. while num_rooms is greater than or equal to 5
     1. call input_dimension and set it equal to the variable length
     2. call input_dimension and set it equal to the variable width
     3. call input_type and set it equal to the variable floor_type
     4. call function calc_cost and set it equal to the variable room_cost
     5. output room_cost to the user
     6. set the variable option equal to user input asking, "Would you like to see the cost with a different floor type? y/n"
     7. convert the variable option to lowercase and strip
     8. While option does not equal y or n
        1. set the variable option equal to user input asking, "Would you like to see the cost with a different floor type? y/n"
     9. if option equals y
        1. call function input_type and set it equal to floor_type
        2. call function calc_cost and set it equal to room_cost
        3. output room_cost to user
     10. if option equals n
         1. set variable total_cost equal to total_cost plus room_cost
         2. set variable num_rooms equal to num_rooms plus 1
  5. Output total_cost to user
  6. output "Thank you for using the program!"

  
