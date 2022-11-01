#MEMORY GAME Function
def get_memory_score(*arg):
    game_list=[]
    game_point=0
    
    for items in arg:
        if(game_list.count(items)):
            game_point=game_point+1
        else:
            game_list.append(items)
            
        if(len(game_list)==6):
            game_list.remove(game_list[0])
        
    return game_point
    
#Input
input_nums = [3, 4, 5, 3, 2, 1]

#Invalid Input Check
invalid_inputs=[]
for items in input_nums:
    if(isinstance(items, float) or isinstance(items, str) or items<0 or items>9):
        invalid_inputs.append(items)
        
if(len(invalid_inputs)!=0):
    print("Please enter a valid input list.\nInvalid inputs detected are {}".format(invalid_inputs))
    exit()

#Execution Of MEMORY GAME
score=get_memory_score(*input_nums)
print('Score:', score)