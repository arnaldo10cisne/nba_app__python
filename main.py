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
    
    NBA_URL = 'https://mach-eight.uc.r.appspot.com/'
    
    l(2)
    print("Please wait while we fetch the data from the URL ...")

    response = requests.get(NBA_URL)

    if response.status_code == 200:

        print("Data fetched succesfully!")
        l(1)
        
        response_json_format = response.json()
        nba_players_array = response_json_format["values"]
        nba_players_array = order_array(nba_players_array)
        
        while True:
            while True:
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
            valid_number = validate_user_input(input_number,int(nba_players_array[0]["h_in"])*2,int(nba_players_array[-1]["h_in"])*2)
            if (valid_number == "Valid"):
                array_of_correct_pairs = find_nba_pairs(input_number, nba_players_array)
                clear_screen()
                
                l(1)
                print("Finding two NBA players whose heights add up to {} inches".format(input_number))
                l(1)

                result_number = 1
                print("RESULTS:")
                l(1)
                
                if len(array_of_correct_pairs) > 0:
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
    
    """)
    standby()


def exit_program():
    print("""
    Thank you for using the NBA App.
    Have a wonderful day! 
    
    Press ENTER to exit""")


if __name__ == "__main__":
    run_program = True
    while run_program:
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
                run_program = False
            else:
                pass
        except:
            pass
    clear_screen()