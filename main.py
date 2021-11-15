from support_module import *
from nba_module import *


def menu():
    return int(input("""
      
      
      _   _ ____                                 
     | \ | |  _ \   /\         /\                
     |  \| | |_) | /  \       /  \   _ __  _ __  
     | . ` |  _ < / /\ \     / /\ \ | '_ \| '_ \ 
     | |\  | |_) / ____ \   / ____ \| |_) | |_) |
     |_| \_|____/_/    \_\ /_/    \_\ .__/| .__/ 
                                    | |   | |    
                                    |_|   |_|    
    
    Welcome to the NBA App. Please select and option:

    1. Start this App
    2. About this App
    3. Exit

    Selection: """))


def run_nba_app():
    """Main flow of the program. Here we call all the functions located in NBA_MODULE.PY"""
    
    #First we need to fetch the information from the URL.
    NBA_URL = 'https://mach-eight.uc.r.appspot.com/'
    l(2)
    print("Please wait while we fetch the data from the URL ...")
    response = requests.get(NBA_URL)

    #If the information is gathered correctly, the app is ready to start
    if response.status_code == 200:

        print("Data fetched succesfully!")
        l(1)
        
        #First we need to order the fetched array, so we are able to search for values on it.
        response_json_format = response.json()
        nba_players_array = response_json_format["values"]
        nba_players_array = order_array(nba_players_array)
        
        while True:
            while True:
                #We ask the user for a number. If the number is not a positive integer, the user will be informed and asked again to enter a number
                try:
                    l(1)
                    input_number = int(input("Please give us a number to work with: "))
                    l(1)
                    break
                except:
                    l(1)
                    print("Invalid entry, please enter a positive integer")
                    standby()
                    clear_screen()
            
            #After the first round of validations is over, the number is then passed to the VALIDATE_USER_INPUT function, to make sure it works
            valid_number = validate_user_input(input_number,int(nba_players_array[0]["h_in"])*2,int(nba_players_array[-1]["h_in"])*2)
            
            #If the input is valid, the flow accesses this conditional. If not, the user is going to be asked for a new number
            if (valid_number == "Valid"):
                
                #We use the function FIND_NBA_PAIRS to create an array that is going to contain inside pairs of indexes, corresponding to players whose heights add up to the number the user gave.
                array_of_correct_pairs = find_nba_pairs(input_number, nba_players_array)
                clear_screen()
                
                l(1)
                print("Finding two NBA players whose heights add up to {} inches".format(input_number))
                l(1)

                result_number = 1
                print("RESULTS:")
                l(1)
                
                #We access this conditional if at least one match was found
                if len(array_of_correct_pairs) > 0:
                    #This loop will go over the ARRAY_OF_CORRECT_PAIRS to print on the screen the first name, last name and height of all the pairs found
                    for result in array_of_correct_pairs:
                        print("Pair {}: {} {} ({} inches) | {} {} ({} inches)".format(result_number, nba_players_array[result[0]]["first_name"], nba_players_array[result[0]]["last_name"], nba_players_array[result[0]]["h_in"], nba_players_array[result[1]]["first_name"], nba_players_array[result[1]]["last_name"], nba_players_array[result[1]]["h_in"]))
                        result_number += 1
                else:
                    print("No matches found")

                l(1)
                print("The pairing is done! Thank you for using the NBA App")
                print("Returning to main menu")

                break
            else:
                print(valid_number)
                standby()
                clear_screen()

    elif response.status_code >= 400:
        #If the program fails trying to fetch the information, the app wont continue
        print("There was an error while trying to fetch information from the URL, please try again later")

    standby()


def about():
    print("""
    
    Program created by Arnaldo Cisneros, as part of a technical test provided by Macheight. 

    This program extracts data on several professional NBA players, and given a positive integer
    supplied by the user, the program is capable of creating pairs of players, in such a way that
    their heights in inches add up to the number supplied by the user.

    The data is gathered from: https://mach-eight.uc.r.appspot.com/

    Developed in the city of Medellín, Colombia. November, 2021.

    Visit me on my social media!
    Linekdin:         https://www.linkedin.com/in/arnaldo10cisne/
    Github:           https://github.com/arnaldo10cisne
    Personal website: https://www.arnaldocisneros.com/

    By the way, before you go, don't forget to check the WEB EDITION of this same app!
    Link: https://arnaldo10cisne.github.io/nba_app__javascript/
    
    """)
    standby()


def exit_program():
    print("""
    Thank you for using the NBA App.
    Have a wonderful day! 
    
    Press ENTER to exit""")


if __name__ == "__main__":
    #This loop is for the main menu. It will run until the user decides to exit the program.
    while True:
        try:
            clear_screen()
            opt = menu()
            if (opt==1):
                clear_screen()
                run_nba_app()
            elif (opt==2):
                clear_screen()
                about()
            elif (opt==3):
                clear_screen()
                exit_program()
                standby()
                break
            else:
                pass
        except:
            pass
    clear_screen()