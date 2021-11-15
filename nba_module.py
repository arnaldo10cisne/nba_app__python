from support_module import *


def validate_user_input(input_number,minimum,maximum):
    """Validates the user input, to make sure it is a positive integer in the range between MINIMUM and MAXIMUM
    
    OUTPUT: str"""
    if input_number < 0:
        return "Please enter a positive integer"
    if input_number < minimum or input_number > maximum:
        return """\nNo matches found\n\nTIP: Enter a number between {} and {} to find possible results""".format(minimum,maximum)
    return "Valid"


def order_array(array_to_order):
    """Uses the merge sort algorithm to order the given list of players from shortest to tallest
    
    OUTPUT: Array"""
    if len(array_to_order) > 1:
        half = len(array_to_order) // 2
        left_arm = array_to_order[:half]
        right_arm = array_to_order[half:]

        order_array(left_arm)
        order_array(right_arm)

        i = 0
        j = 0
        k = 0

        while i < len(left_arm) and j < len(right_arm):
            if left_arm[i]["h_in"] < right_arm[j]["h_in"]:
                array_to_order[k] = left_arm[i]
                i += 1
            else:
                array_to_order[k] = right_arm[j]
                j += 1
            k += 1

        while i < len(left_arm):
            array_to_order[k] = left_arm[i]
            i += 1
            k += 1

        while j < len(right_arm):
            array_to_order[k] = right_arm[j]
            j += 1
            k += 1

        return array_to_order


def search_first_result(list, start, end, objective):
    """Uses the binary search algorithm recursively to find the position of one of the players whose height in inches is equal to OBJECTIVE
    
    OUTPUT: int"""

    if start > end:
        return None

    split = (start + end) // 2

    if split >= len(list):
        return None

    if int(list[split]["h_in"]) == objective:
        return split
    elif int(list[split]["h_in"]) < objective:
        return search_first_result(list, split+1, end, objective)
    elif int(list[split]["h_in"]) > objective:
        return search_first_result(list, start, split-1, objective)

    


def find_nba_pairs(user_input, list_of_players):
    """Given an USER_INPUT and a LIST_OF_PLAYERS, this function generates and array called ARRAY_OF_CORRECT_PAIRS, that is going to store inside a list of smaller arrays with only 2 numbers, that represent the index of 2 players whose height add up to the USER_INPUT
    
    OUTPUT: Array"""

    array_of_correct_pairs = []

    #This loop is going to be used to evaluate each player individually
    for first_player in list_of_players:

        #We calculate the difference between the USER_INPUT and height of the player currently being evaluated
        difference = user_input - int(first_player["h_in"])
        
        #We use the function SEARCH_FIRST_RESULT to assing to FIRST_RESULT_POSITION the index of one player whose height matches the DIFFERENCE
        first_result_position = search_first_result(list_of_players, 0, len(list_of_players), difference)

        #We access this conditional if at least one match was found
        if first_result_position != None:
            
            first_result_position = int(first_result_position)
            
            #AUX is used to help with the SPREAD Algorithm, and CONTINUE_CHECKING_HEIGHTS is a boolean we use to avoid a "indexerror: list index out of range" error
            aux = 0
            continue_checking_heights = True

            #This loop is used to find all matches to the right of the original match (Those that have a higher index)
            while True:
                if continue_checking_heights and int(list_of_players[first_result_position + aux]["h_in"]) == difference:
                    #We only create a solution match if the first player has a lower height than the second player. This is in order to avoid repeated pairs.
                    if list_of_players.index(first_player) <= first_result_position + aux:
                        array_of_correct_pairs.append([list_of_players.index(first_player),first_result_position + aux])
                    #Once the pair has been evaluated, we increase AUX to check the next player's height
                    if first_result_position + aux < len(list_of_players) - 1:
                        aux += 1
                    else:
                        #If AUX is going to generate the "indexerror: list index out of range" error, the CONTINUE_CHECKING_HEIGHTS boolean is reassign to False to prevent this
                        continue_checking_heights = False
                else:
                    #AUX is restarted to 1 to be used again in the next loop
                    aux = 1
                    break
            #This loop is used to find all matches to the left of the original match (Those that have a lower index)
            while True:
                if int(list_of_players[first_result_position - aux]["h_in"]) == difference:
                    if list_of_players.index(first_player) <= first_result_position - aux:
                        array_of_correct_pairs.append([list_of_players.index(first_player),first_result_position - aux])
                    aux += 1
                else:
                    break
                
    
    #Once ARRAY_OF_CORRECT_PAIRS has been successfully filled, we return it
    return array_of_correct_pairs