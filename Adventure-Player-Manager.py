player_Names = set()

players = {}

import random

def add_player():
    while True:
        player_Name = input("Enter player name: ")
        if player_Name in player_Names:
            print("That name has already been entered")
            continue
        break
    
    while True:
        try:
            level = int(input("Enter your level number: "))
            break
        except ValueError:
            print("Level Number must be a valid number")
            
    while True:
            try:
                score = int(input("Enter your score: "))
                break
            except ValueError:
                print("Level Number must be a valid number")
    
    player_Names.add(player_Name)            
    players[player_Name] = (score, level)
    
    
def remove_player():
    while True:
        player_Name = input("Enter the name of the player to remove: ")
        if player_Name in player_Names:
            print("Player removed")
            break
        print("That player doesnt exist")
        continue
    player_Names.remove(player_Name)
    del players[player_Name]
    



def view_Players():
    if not players :
        print("There has been no players inputted")
    
    for name, info in players.items():
        score, level = info
        print(name, score, level)
        

def show_Stats():
    if not players:
        print("No stats available")
    
    scores = [info[0] for info in players.values()]
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores)/ len(scores)
    
    print("The highest score is: ", highest)
    print("The lowest score is: ", lowest)
    print("The average score is: ", average)
    
        
while True:
    try:
        choice = int(input("1.Add player\n2.Remove player\n3.View players\n4.Show stats\n5.Exit\nChoice: "))
        if choice <1 or choice >5:
            print("Invalid choice. Must be a number between 1-4")
            
        if choice == 1:
            add_player()
            
        if choice == 2:
            remove_player()
            
        if choice == 3:
            view_Players()
            
        if choice == 4:
            show_Stats()
            
        if choice == 5:
            print("Goodbye")
            break
                
    except ValueError:
        print("Invalid choice. Must be a number between 1-4")
        
        
        
    
        
    
        
    
    
    
        
        
        
        
    

    




