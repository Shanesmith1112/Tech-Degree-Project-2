import copy
import constants
import sys


player_info = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
panthers = []
bandits = []
warriors = []
exp_players = []
noexp_players = []
num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))


print("******** BASKETBALL TEAM STATS TOOL ********")


def clean_data():
    for player in player_info:
        player["height"] = int(player["height"][:2])
        if player['experience'] == "YES":
            player['experience'] = "TRUE"
            exp_players.append(player)
        if player['experience'] == "NO":
            player['experience'] = "FALSE"
            noexp_players.append(player)
        player['guardians'] = player['guardians'].split(" and ")


def balance_exp():
    num_exp_players = int(len(exp_players) / len(constants.TEAMS))
    for player in exp_players:
        if len(panthers) < num_exp_players:
            panthers.append(player)
        elif len(bandits) < num_exp_players:
            bandits.append(player)
        elif len(warriors) < num_exp_players:
            warriors.append(player)


def balance_noexp():
    for player in noexp_players:
        if len(panthers) < num_players_team:
            panthers.append(player)
        elif len(bandits) < num_players_team:
            bandits.append(player)
        elif len(warriors) < num_players_team:
            warriors.append(player)


def press_enter():
    press_e = input("Press ENTER to Continue...")
    if press_e == " ":
        menu()
    else:
        menu()


def main():
    print('\n1.) Bandits\n2.) Panthers\n3.) Warriors\n')
    while True:
        try:
            team_choice = int(input('Please enter an option > '))
            if team_choice < 1 or team_choice > 3:
                print('\nERROR!\nThat is not a valid option\n')
            elif team_choice == 1:
                print("You have chosen the Bandits!")
                print("There are {} players on the team.".format(int(len(bandits))))
                press_enter()
            elif team_choice == 2:
                print("You have Chosen the Panthers!")
                print("There are {} players on the team.".format(int(len(panthers))))
                press_enter()
            elif team_choice == 3:
                print("You have chosen the Warriors!")
                print("There are {} players on the team.".format(int(len(warriors))))
                press_enter()
        except ValueError:
            print('\nERROR!\nThat is not a valid option, please choose and option from the list\n')
            pass


def menu():
    print("\n\n --- MENU --- \n\n")
    print('Here are your choices:\n 1.) Display Team Stats\n 2.) Quit\n')
    while True:
        try:
            choice = int(input('Please enter an option > '))
            if choice == 2:
                print('\nThank you for using Basketball Team Stats Tool')
                exit()
            elif choice < 1 or choice > 2:
                print('\nERROR!\nThat is not a valid option.\n')
            elif choice == 1:
                main()
        except ValueError:
            print('\nERROR!\nThat is not a valid option please enter an option from the list\n')
            continue


if __name__ == '__main__':
    clean_data()
    balance_exp()
    balance_noexp()
    menu()
