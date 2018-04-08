'''
Created on 7 Apr 2018

@author: pdj10
'''

dungeon_max_x = 10
dungeon_max_y = 20

dungeon = myArray=[[0 for j in range(dungeon_max_x)] for i in range(dungeon_max_y)]

dungeon [1][3]='#'
        
for row in dungeon :
    print ("")
    for cell in row :
        print (cell, end='')


if __name__ == '__main__':
    print ("Hello World!")
    