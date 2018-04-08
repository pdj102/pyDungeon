'''
Created on 7 Apr 2018

@author: pdj10
'''

from pyDungeon import dungeon_map

from pyDungeon import item 


if __name__ == '__main__':

    print ("Hello World!")
    
    dungeon_map.init_map()
    dungeon_map.create_room(5,2,10,10)
    
    dungeon_map.print_map()
    
    items = [] 
    
    items.append( item.Item('@') )
    
    items[0].print_item() 
    