'''This script uses data from the rooms.py file and readfile.py to allocate.'''


from readfile import GetData
from rooms import *

occupied_offices = []
occupied_malerooms = []
occupied_femalerooms = []

officedata = GetData().officedata()
maledata = GetData().maledata()
femaledata = GetData().femaledata()

unplacedmaledata = maledata[:]
unplacedofficedata = officedata[:]
unplacedfemaledata = femaledata[:]

class Allocate(object):

    '''Class defined to allocate data to different office.'''

    def allocate_office(self):

        '''Method defined to check count while allocating.'''

        for office in amityoffices:
            officeroom = OfficeRoom(office)
            while len(officeroom.officemembers) < officeroom.maxofficepersons:
                if len(unplacedofficedata):
                    position = unplacedofficedata.pop()
                    officeroom.addofficemember(position)
                else:
                    break
            occupied_offices.append(officeroom)
            if len(unplacedofficedata) == 0:
                break

    def allocate_malerooms(self):

        '''Method defined to check count while allocating.'''

        for maleroom in amitymalerooms:
            livingspacemale = LivingSpacesMale(maleroom)
            while len(livingspacemale.maleroommembers) < livingspacemale.maxmalepersons:
                if len(unplacedmaledata):
                    position = unplacedmaledata.pop()
                    livingspacemale.addmalemembers(position)
                else:
                    break
            occupied_malerooms.append(livingspacemale)
            if len(unplacedmaledata) == 0:
                break

    def allocate_femalerooms(self):

        '''Method defined to check count while allocating.'''

        for femaleroom in amityfemalerooms:
            livingspacefemale = LivingSpacesFemale(femaleroom)
            while len(livingspacefemale.femaleroommembers) < livingspacefemale.maxfemalepersons:
                if len(unplacedfemaledata):
                    position = unplacedfemaledata.pop()
                    livingspacefemale.addfemalemember(position)
                else:
                    break
            occupied_femalerooms.append(livingspacefemale)
            if len(unplacedfemaledata) == 0:
                break




