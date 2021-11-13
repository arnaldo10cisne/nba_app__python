import requests
import json 

def nba_function(user_input):
    pass

def run():
    NBA_URL = 'https://mach-eight.uc.r.appspot.com/'
    response = requests.get(NBA_URL)

    print(type(response))

    info = response.json()
    
    if response.status_code == 200:
        pass
        #print(response.content)


if __name__ == "__main__":
    run()