'''Script use to view result of allocation.'''

from Allocate import Allocate, GetData, occupied_offices, officedata, unplacedofficedata, occupied_malerooms, maledata, unplacedfemaledata, unplacedmaledata, occupied_femalerooms, femaledata, notallocatedtolivingspace, staffnotallocatedtorooms
from readfile import filename

start = Allocate()
start.allocate_office()
start.allocate_malerooms()
start.allocate_femalerooms()



class ViewResults(object):

    ''' Class defined to view results of allocation. '''

    @staticmethod
    def allocatedlist():

        '''Method prints allocation list for office.'''

        print "AMITY OFFICE AND MEMBERS ASSIGNED. "
        for room in occupied_offices:
            print "For the {} Office those allocated are: " .format(room.name)
            for i, value in enumerate(room.officemembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
            print("" * 1)


        print "AMITY MALEROOMS AND MEMBERS ASSIGNED. "
        for room in occupied_malerooms:
            print "For the {} maleroom those allocated are: " .format(room.name)
            for i, value in enumerate(room.maleroommembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
            print("" * 1)


        print "AMITY FEMALEROOMS AND MEMBERS ASSIGNED. "
        for room in occupied_femalerooms:
            print "For the {} femaleroom those allocated are: " .format(room.name)
            for i, value in enumerate(room.femaleroommembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
            print("" * 1)
    
    @staticmethod
    def Unallocatedlist():

        '''Method prints Not allocated list for office.'''
        
        if len(unplacedofficedata):
            print "You can view the {} unallocated members below." .format(len(unplacedofficedata))
            for i, value in enumerate(unplacedofficedata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedofficedata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)
        print "Allocated members to malerooms are {}" .format(len(maledata)-len(unplacedmaledata))
        if len(unplacedmaledata):
            print "You can view the {} unallocated members below." .format(len(unplacedmaledata))
            for i, value in enumerate(unplacedmaledata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedmaledata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)

        
        print "Allocated members to femalerooms are {}" .format(len(maledata)-len(unplacedmaledata))

        if len(unplacedfemaledata):
            print "You can view the {} unallocated members below." .format(len(unplacedfemaledata))
            for i, value in enumerate(unplacedfemaledata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedfemaledata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)

    @staticmethod
    def officeroom_members(room):

        '''Method prints members of any specified officeroom.'''

        for offices in occupied_offices:
            if offices.name == room:
                print "For the {} office those allocated are: " .format(offices.name)
                for i, value in enumerate(offices.officemembers):
                    if offices.officemembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                    else:
                        print "No one present in this room."
        print("" * 1)

    @staticmethod
    def maleroom_members(room):

        '''Method prints members of any specified maleroom.'''

        for rooms in occupied_malerooms:
            if rooms.name == room:
                print "For the {} maleroom those allocated are: " .format(rooms.name)
                for i, value in enumerate(rooms.maleroommembers):
                    if rooms.maleroommembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                    else:
                        print "No one present in this room."
        print("" * 1)


    @staticmethod
    def femaleroom_members(room):

        '''Method prints members of any specified femaleroom.'''

        for rooms in occupied_femalerooms:
            if rooms.name == room:
                print "For the {} femaleroom those allocated are: " .format(rooms.name)
                for i, value in enumerate(rooms.femaleroommembers):
                    if rooms.femaleroommembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                    else:
                        print "No one present in this room."
        print("" * 1)




#officedata = GetData.read_file(filename = 'input2.txt')
ViewResults.Unallocatedlist()
ViewResults.allocatedlist()
ViewResults.maleroom_members('topaz')
ViewResults.officeroom_members('Vulcan')
ViewResults.femaleroom_members('pearl')
