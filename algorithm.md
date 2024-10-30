# Algorithm

1. Start the program
- Print a welcome message saying that is explaing the purpose of the program
2. intialize variables
- Set total_cost to 0
- Set num_rooms to 0
3. Room proscessing loop
- while num_rooms is less than or equal to five
    1. Input room dimensions
        1. Call the input_dimesnsions function twice to get the length of the suers room, make sure proper integers are called
    1. Input floor type
        1. call input_type fucntions to get the floor type from the user, hardwood, tile,or carpet
  1. calculate the room cost
        1. call calc_lost to calculate the the cost for the flooring of the room
     2. print the cost
4. Offering floor type change
    1. Ask the user if they want to see the cost with the differnet floor types
        1. If the user chooses y, repeat the floor type selection and cost calculation steps, then print the updated room cost.
        1. If the user chooses n, add the current room cost to total_cost and increment num_rooms by 1.
4. Final Output
    1. after proscessing everything print the total_cost for the flooring of all the rooms
2. End

  
