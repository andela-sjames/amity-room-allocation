'''Script used to hold rooms and office properties'''
import random

amityoffices = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge', 'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan',]
random.shuffle(amityoffices)

amitymalerooms = ['topaz', 'silver', 'gold', 'onyx', 'opal',]
random.shuffle(amitymalerooms)

amityfemalerooms = ['ruby', 'platinum', 'jade', 'pearl', 'diamond',]
random.shuffle(amityfemalerooms)



class OfficeRoom(object):

    ''' Class takes a maximum of 6 persons per room. '''

    def __init__(self, name, maxofficepersons=6):
        self.name = name
        self.maxofficepersons = maxofficepersons
        self.officemembers = []

    def addofficemember(self, member):
        '''Method appends member data to class.'''
        self.officemembers.append(member)



class LivingSpacesMale(object):

    ''' Class takes a maximum of 4 persons per room. '''

    def __init__(self, name, maxmalepersons=4):
        self.name = name
        self.maxmalepersons = maxmalepersons
        self.maleroommembers = []

    def addmalemembers(self, member):
        '''Method appends member data to class.'''
        self.maleroommembers.append(member)


class LivingSpacesFemale(object):

    ''' Class takes a maximum of 4 persons per room. '''

    def __init__(self, name, maxfemalepersons=4):
        self.name = name
        self.maxfemalepersons = maxfemalepersons
        self.femaleroommembers = []

    def addfemalemember(self, member):
        '''Method appends member data to class.'''
        self.femaleroommembers.append(member)




