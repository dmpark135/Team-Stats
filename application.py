import copy
from constants import PLAYERS, TEAMS

copied_players= copy.deepcopy(PLAYERS)

def clean_data(copied_players):
        for player in copied_players:
            if player['experience'] == "YES":
                player['experience'] = True
            else:
                player['experience'] = False
            player['height'] = player['height'].split()[0]
            player['height'] = int(player['height'])
clean_data(copied_players)

def main():
    print('\nBASKETBALL TEAM STATS TOOL\n\n---- MENU----\n\n')
    print(' Here are your choices:')
    print('  1) Display Team Stats\n  2) Quit\n\n')
    option = input(' Enter an option number: ')
    print('\n')
    
    if option == '1':
        print(' 1) Panthers \n 2) Bandits\n 3) Warriors')
        i = input('Enter a Team number: ')        
        valid_choices = ['1', '2', '3']
        while i not in valid_choices:
            i = input("Enter a valid team number (1, 2, or 3): ")
    else:
        print('Thanks for coming by!')
        return
    
    i = int(i)
    Team_name = TEAMS[i-1]    
    print('\nTeam: ', Team_name)
    print('-------------------')
    
    def balance_teams(copied_players):
        player_list = copied_players[i::len(TEAMS)]
        name_list = [player['name'] for player in player_list]
        print('Total players: ',len(player_list))
        print('\n')
        print(', '.join(name_list))
    balance_teams(copied_players)
    end = input('\n Press Enter to continue: ')
    if end =='':
        main()
    else:
        print('bye')
        return

if __name__ == '__main__':
    main()
    



      

    
      


    

    



    
        
     

        
    
    
        
        
        
    
            
        
        
        
    
        
            
       
        
        
        
        
        
        
        
    
    
    
    
    