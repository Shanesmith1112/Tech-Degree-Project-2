import copy
import constants


player_info = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
panthers = []
bandits = []
warriors = []
exp_players = []
noexp_players = []


def clean_data():
    for player in player_info:
        player["height"] = int(player["height"][:2])
        if player['experience'] == "YES":
            player['experience'] = bool("True")
            exp_players.append(player)
        if player['experience'] == "NO":
            player['experience'] = bool()
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
    num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))
    for player in noexp_players:
        if len(panthers) < num_players_team:
            panthers.append(player)
        elif len(bandits) < num_players_team:
            bandits.append(player)
        elif len(warriors) < num_players_team:
            warriors.append(player)


def height_tool(team):
    temp_heights = []
    for player in team.copy():
        temp_heights.append(player['height'])
    total = sum(temp_heights)
    average_height = total / len(team)
    print("\nThe average player height is {} inches.".format(int(average_height)))


def team_stats(team):
    print("\nThere are {} players on the team in total.".format(int(len(team))))
    print("\nThere are {} experienced players on the team.".format(int(len(exp_players) / len(teams))))
    print("There are {} inexperienced players on the team.".format(int(len(noexp_players) / len(teams))))
    team_players = []
    for player in team.copy():
        team_players.append(player['name'])
    players = ", ".join(team_players)
    print("\nThe players on the team are...")
    print(players)


def team_guardians(team):
    team_parents = []
    for player in team.copy():
        team_parents.append(', '.join(player['guardians']))
    parents = ", ".join(team_parents)
    print("\nThe parent/guardians for the team are...")
    print(parents)


def press_enter():
    press_e = input("\nPress ENTER to Continue...\n")
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
                print("\nYou have chosen the Bandits!")
                team_stats(bandits)
                height_tool(bandits)
                team_guardians(bandits)
                press_enter()
            elif team_choice == 2:
                print("\nYou have Chosen the Panthers!")
                team_stats(panthers)
                height_tool(panthers)
                team_guardians(panthers)
                press_enter()
            elif team_choice == 3:
                print("\nYou have chosen the Warriors!")
                team_stats(warriors)
                height_tool(warriors)
                team_guardians(warriors)
                press_enter()
        except ValueError:
            print('\nERROR!\nThat is not a valid option, please choose and option from the list\n')
            pass


def menu():
    print("\n******** BASKETBALL TEAM STATS TOOL ********\n")
    print("\n\n --- MENU --- \n\n")
    print('Here are your choices:\n 1.) Display Team Stats\n 2.) Quit\n')
    while True:
        try:
            choice = int(input('Please enter an option > '))
            if choice == 2:
                print('\nThank you for using Basketball Team Stats Tool!')
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
