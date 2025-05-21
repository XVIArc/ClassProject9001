import math
import random

class Room:
    def __init__(self,x:int,y:int,difficulty='#Wall'):      #The basic is every room was a wall
        self.x = x
        self.y = y
        self.difficulty = difficulty    #The room should have these varieties: Empty(Start) Easy Normal Hard Boss Miniboss Shop Treasure.

    def __str__(self):
        return f'{self.difficulty[0]}'

def valid_dir(x:int,y:int,n) -> bool:
    '''
    This step is easier because I am considering a square otherwise it should be length and width
    It is used for if the room is OK to place.
    '''
    return 0<=x<n and 0<=y<n
def cross_lock(x:int,y:int,n) -> bool:
    '''
    This is used for checking if room is too Intensive.
    The logic is: I blocked four crossed rooms at start room. These rooms are not available anyways.
    |X| |X|
    | |S| |
    |X| |X|
    '''
    start = math.ceil(n/2)-1
    if x+1==start or x-1 == start:
        if y+1 == start or y-1 == start:
            return True
    return False


# def noroom(map:list[list[Room]],x:int,y:int,dir:str) -> bool:
#     '''
#     Check if some direction has a room.
#     warning: you HAVE to use this AFTER but NOT with at_border
#     '''
#
#     if dir=='north':
#         x-=1
#     elif dir=='south':
#         x+=1
#     elif dir=='east':
#         y+=1
#     elif dir=='west':
#         y-=1
#     return map[y][x] is None

def GenerateRooms(n:int) -> list[list[Room]]:
    '''
    Generating the basic map.
    Honestly, this idea is totally from Ass1
    '''
    gamemap = []

    for i in range(n):
        row = [None for _ in range(n)]          #This is learned from internet.
        gamemap.append(row)

    Start = math.ceil(n/2)-1
    gamemap[Start][Start] = Room(Start,Start,'Start')                          #This is my start room.

    return gamemap                                                     #Return n*n.

def display_map(grid: list[list[Room]]):
    '''
    Prints the current state of the grid in a readable map format.

    This is stolen from ass1 to check where am I im the progress.
    '''
    # print(len(grid))=n
    # print(len(grid[1]))=n

    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if grid[i][n] is not None:
                print(f'|{grid[i][n]}',end='')
            else:
                print(f'|#',end='')
        print('|')


# def Roomgenerator(map:list[list[Room]],n:int):
#     '''begin from start room, which we know it is at ceil(n/2)-1, room count should be (n^2/2)-1'''
#     start = math.ceil(n/2)-1
#     start_x = start_y = start
#     seed = input('Enter a seed number(None is for random seed):')
#     Gen = random.Random(seed)
#     direction = ['north','south','east','west']
#     # Dir = Gen.choice(direction)
#     dx_dy ={
#         'north':(-1,0),
#         'south':(1,0),
#         'east':(0,1),
#         'west':(0,-1)
#     }
#     generatedroom = 1
#     room_count = math.ceil(n*n/2) - 1          #EG: 5*5 Should have 13 rooms since we got a start it is 12.
#     cur_x = start_x
#     cur_y = start_y
#
#
#     while generatedroom < room_count:
#         # print(i)
#         Dir = Gen.choice(direction)
#         dx,dy = dx_dy[Dir]
#         new_x = cur_x + dx              #Learned from online.
#         new_y = cur_y + dy
#
#         if 0<=new_x<n and 0<=new_y<n:
#             if map[new_x][new_y] is None:
#                 map[new_x][new_y] = Room(new_x,new_y)
#                 cur_x,cur_y = new_x,new_y
#                 generatedroom += 1
#                 print('generated')
#             else:
#                 cur_x,cur_y = new_x,new_y
#                 # print('not generatedA')
#         else:
#             cur_x,cur_y = start_x,start_y
#             # print('not generatedB')

def roomgenerator2(map:list[list[Room]],n:int):             #It is a square map
    '''
    THIS IS A SUPER COMPLICATED FUNCTION(AS I COULD SEE)
    I IMPLEMENTED THESE:
    1.random seeds for generating
    2.
    '''

    #1 Random seeds and basic information
    start = math.ceil(n/2)-1
    x = y = start           #Locating the start room.
    seed_input = input('Enter a seed number(No input is for random seed):')
    if not seed_input:            #Randomize
        seed = random.randint(0,999999)
    else:
        seed = seed_input
    GeneratorSeed = random.Random(seed)
    print(f'Seed: {seed}')


    direction = ['north', 'south', 'east', 'west']
    type = ['Boss','Treasure','$Shop','Challenge']
    GeneratorSeed.shuffle(direction)                   #Shuffle.
    mapping = dict(zip(direction,type))         #Dictionary-lize this
    path_info = {
        'Boss': math.ceil(n / 2) + 1,
        'Treasure': random.randint(1, math.floor(n / 2)),
        '$Shop': random.randint(math.ceil(n / 2) // 2, math.ceil(n / 2)),
        'Challenge': random.randint(math.ceil(n / 2) // 2, math.ceil(n / 2)),
    }
    dx_dy = {                       #Directions
        'north': (0, -1),
        'south': (0, 1),
        'east': (1, 0),
        'west': (-1, 0),
    }
    # cant_go={
    #     'north':'south',
    #     'south':'north',
    #     'east':'west',
    #     'west':'east'
    # }
    # for dir in direction:           #Testcode
    #     print(f"{dir},{mapping[dir]}")


    #2 Making rooms. I need Startroom, Direction, Roomtype and Pathlength. Require N.
    for dir in direction:           #Instance:North boss
        type = mapping[dir]
        length = path_info[type]
        cango=['north','east','south','west']
        maindir = cango.index(dir)
        dir0 = cango[maindir]
        dira = cango[(maindir+4-1)%4]
        dirb = cango[(maindir+4+1)%4]       #No opposite direction.
        directions = [dir0,dira,dirb]
        cur_x,cur_y = x,y       #FOR EACH DIRECTION.
        step = 1
        Tries = 30

        print(f'Generating Path:{type}, Direction:{dir0} -> {length} Steps.')       #TEST.Finally this is changed to a interesting message.
        while step<=length:      #Any kind of steps.
            if Tries == 0:
                print('I got a mistake when generating the map. Would you mind starting over?')
                break
            if step!=1:
                GeneratorSeed.shuffle(directions)
            Goto = directions[0]
            dx, dy = dx_dy[Goto]  # This is asked with internet.


            newx,newy = cur_x + dx, cur_y + dy
            if not cross_lock(newx,newy,n) and valid_dir(newx,newy,n) and map[newx][newy] is None: #Available
                if step != length:
                    map[newx][newy] = Room(newx,newy,' Normal')

                else:
                    map[newx][newy] = Room(newx,newy,type)
                cur_x,cur_y = newx,newy
                step += 1
            else:
                Tries-=1



        # for step in range(1,length+1):
        #     possible_dir = []
        #     for dir,(dx,dy) in dx_dy.items():
        #         newx,newy = x + dx, y + dy
        #         if valid_dir(newx,newy,n) and map[newx][newy] is None:





if __name__ == '__main__':          #TESTCODES
    gamemap = GenerateRooms(15)
    roomgenerator2(gamemap,15)
    # Roomgenerator(gamemap,5)
    display_map(gamemap)