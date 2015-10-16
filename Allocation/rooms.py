'''Script used to hold rooms and office properties'''

class Office(object):

    ''' Class takes a maximum of 6 persons per room. '''

    def __init__(self, name, maxpersons=6):
        self.name = name
        self.maxpersons = maxpersons
        self.roommembers = []

    def addmember(self, member):
        
        '''Method appends member data to class.'''

        self.roommembers.append(member)



class LivingSpace(Office):

    ''' Class takes a maximum of 4 persons per room. '''

    roomtype = None
    def __init__(self, roomtype, name, maxpersons=4):
        super(LivingSpace, self).__init__(roomtype, name)
        self.roomtype = roomtype
        self.name = name
        self.maxpersons = maxpersons
        self.malemember = []
        self.femalemember = []

    def addfellow(self, member):

        '''Method checks for room type before adding member'''

        if self.roomtype == 'm':
            self.malemember.append(member)
        else:
            self.femalemember.append(member)        




