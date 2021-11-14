from support_module import *


def validate_user_input(input_number,minimum,maximum):
    if input_number < 0:
        return "Please enter a positive integer"
    if input_number < minimum or input_number > maximum:
        return """No matches found\n\nTIP: Enter a number between {} and {} to find possible results""".format(minimum,maximum)
    return "Valid"


def order_array(array_to_order):
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
    
    if start > end:
        return None

    split = (start + end) // 2

    if int(list[split]["h_in"]) == objective:
        return split
    elif int(list[split]["h_in"]) < objective:
        return search_first_result(list, split+1, end, objective)
    elif int(list[split]["h_in"]) > objective:
        return search_first_result(list, start, split-1, objective)


def find_nba_pairs(user_input, list_of_players):

    #print("User input: ", user_input)

    array_of_correct_pairs = []

    for first_player in list_of_players:
        
        #print("Evaluando alguien con altura: ", first_player["h_in"])

        difference = user_input - int(first_player["h_in"])

        #print("Difference: ", difference)
        
        first_result_position = search_first_result(list_of_players, 0, len(list_of_players), difference)

        #print("Func. Entro 1")
        #print(first_result_position)

        if first_result_position != None:
            
            first_result_position = int(first_result_position)
            if list_of_players.index(first_player) <= first_result_position:
                array_of_correct_pairs.append([list_of_players.index(first_player),first_result_position])
            
            aux = 1
            
            while True:
                #print("Func. Entro 2")
                #if (first_result_position+aux) <= len(list_of_players):
                #print("Func. Entro 3")
                #print(len(list_of_players))
                #print(first_result_position+aux)
                #print(int(list_of_players[first_result_position + aux]["h_in"]))
                if int(list_of_players[first_result_position + aux]["h_in"]) == difference:
                    #print("Func. Entro 4")
                    if list_of_players.index(first_player) <= first_result_position + aux:
                        array_of_correct_pairs.append([list_of_players.index(first_player),first_result_position + aux])
                    aux += 1
                else:
                    aux = 1
                    break
            while True:
                #if (first_result_position+aux) >= 0:
                if int(list_of_players[first_result_position - aux]["h_in"]) == difference:
                    if list_of_players.index(first_player) <= first_result_position - aux:
                        array_of_correct_pairs.append([list_of_players.index(first_player),first_result_position - aux])
                    aux += 1
                else:
                    break
    
    return array_of_correct_pairs