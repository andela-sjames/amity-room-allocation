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
    type = None
    def __init__(self, type, name, maxpersons=4):
        super(LivingSpace, self).__init__(type, name)
        self.type = type
        self.name = name
        self.maxpersons = maxpersons
        self.malemember = []
        self.femalemember = []

    def addmalemember(self, member):
        if self.type == 'm':
            self.malemember.append(member)

    def addfemalemember(self,member):
        if self.type == 'f':
            self.femalemember.append(member)




