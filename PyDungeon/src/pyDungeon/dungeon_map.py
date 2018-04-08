'''
Created on 8 Apr 2018

@author: pdj10
'''

from pyDungeon.tile import Tile, tile_floor, tile_wall


# set the size of the dungeon_map
map_max_x = 20
map_max_y = 20

# create the dungeon_map
dungeon_map = [[0 for j in range(map_max_x)] for i in range(map_max_y)]


def init_map():
    for row in range(map_max_x):
        for col in range(map_max_y):   
            dungeon_map[row][col]=tile_wall


def create_room(x, y, width, height):
    for row in range(y,height):
        for col in range(x, width):
            dungeon_map[row][col]=tile_floor


                
def print_map():
    for row in range(map_max_y):
        for col in range(map_max_x):   
            print(dungeon_map[row][col].get_char(),end='')
        print("")               
