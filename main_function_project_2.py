import sys
#import constants 

print("******** BASKETBALL TEAM STATS TOOL ********")

Bandits = []
Panthers = []
Warriors = []

Players = []
#players[] may not be needed in the end 


#def clean_data():
    #store all data in proper data forms ie numbers as ints and variables as strings 
    # .append new data to players[] ??


#def balance_teams():
    #balance teams and store them in proper lists with appropriate information


def main():
    print('\n1.) Bandits\n2.) Panthers\n3.) Warriors\n')
    while 1 == 1:
        try:
            team_choice = int(input('Please enter an option > '))
            if team_choice < 1 or team_choice > 3:
                print('\nERROR!\nThat is not a valid option\n')
           #elif team_choice == 1:
                # display Bandits stats
                # press enter to continue
           #elif team_choice == 2:
                # display Panthers stats
                # press enter to continue
           #elif team_choice == 3:
                # display Warriors stats
                # press enter to continue
        except ValueError:
            print('\nERROR!\nThat is not a valid option, please choose and option from the list\n')
            pass


def menu():
    print("\n\n --- MENU --- \n\n")
    print('Here are your choices:\n 1.) Display Team Stats\n 2.) Quit\n')
    while 1 == 1:
        try:
            choice = int(input('Please enter an option > '))
            if choice == 2:
                print('\nThank you for using Basketball Team Stats Tool')
                exit()
            elif choice < 1 or choice >2:
                print('\nERROR!\nThat is not a valid option.\n') 
            elif choice == 1:
                main()
        except ValueError:
            print('\nERROR!\nThat is not a valid option please enter an option from the list\n')
            continue 


if __name__ == '__main__':
    #clean_data()
    #balance_teams()
    menu()
            