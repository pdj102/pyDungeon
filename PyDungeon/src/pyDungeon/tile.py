'''
Created on 8 Apr 2018

@author: pdj10
'''

class Tile(object):
    '''
    classdocs
    '''


    def __init__(self, c):
        '''
        Constructor
        '''
        self.char = c
        
        
    def set_char(self, c):
        self.char = c
        
    def get_char(self):
        return self.char
        
tile_wall = Tile('#')
tile_floor = Tile('.')            