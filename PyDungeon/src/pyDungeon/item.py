'''
Created on 8 Apr 2018

@author: pdj10
'''

class Item(object):
    '''
    classdocs
    '''
# shared class variables go here



    def __init__(self, c):
        '''
        Constructor
        '''
        self.set_char(c)


    def set_char(self, c):
        self.char = c
        
    def get_char(self):
        return self.char
    
    def print_item(self):
        print( self.char)
        
