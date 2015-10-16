'''
Models for the different perople
'''

class Person(object):
    '''
    Class to model Person
    '''
    def __init__(self, name, gender, position, wants_living = False):
        self.name = name
        self.gender = gender
        self.position = position
        self.wants_living = wants_living


class Fellow(Person):
    
    '''
    Class to model Fellow
    '''
    pass
