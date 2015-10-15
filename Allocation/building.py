'''This script uses data from the persons.py file and rooms.py to allocate.'''

from fileparser import Parser
from rooms import Office, LivingSpace
import random
    

class Building(object):

    '''Class mimics an actual building and contains methods to view result. '''
    occupied_offices =[]
    occupied_hostels = []
    office_memberA = []
    the_fellowsB = []
    room_directory = {
        'offices': [],
        'livingspaces': [],
        }
    
    def __init__(self, inputfile):
        self.people = Parser.read_file(inputfile)
    
    def populate_rooms(self):

        '''Method used to populate room before allocation'''

        offices = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge', 'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan',]

        livingspacerooms = [('m','topaz'), ('m','silver'), ('m','gold'), ('m','onyx'), ('m','opal'),('f','ruby'), ('f','platinum'), ('f','jade'), ('f','pearl'), ('f','diamond'),]

        for room_name in offices:
            self.room_directory['offices'].append(room_name)

        for room_name in livingspacerooms:
            self.room_directory['livingspaces'].append(room_name)


    def allocate_to_office(self):

        '''Method used to allocate members to offices. ''' 
        
        random.shuffle(self.people['everyone'])
        for office_name in self.room_directory['offices']:            
            office = Office(office_name)
            while len(office.roommembers) < office.maxpersons:
                if len(self.people['everyone']):
                    person = self.people['everyone'].pop()
                    office.addmember(person)
                else:
                    break
            self.occupied_offices.append(office)
            if len(self.people['everyone']) == 0:
                break

    def allocate_to_livingspace(self):

        ''' Method used to allocate fellows to rooms.'''

        random.shuffle(self.people['fellows'])
        for hostelname in self.room_directory['livingspaces']:
            hostel = LivingSpace(hostelname[0],hostelname[1]) #male
            while len(hostel.femalemember) < hostel.maxpersons and len(hostel.malemember) < hostel.maxpersons:
                if len(self.people['fellows']): 
                    fellow = self.people['fellows'].pop() #female
                    if fellow.gender == 'F' and fellow.wants_living:
                        hostel.addfemalemember(fellow)


                    if fellow.gender == 'M' and fellow.wants_living:
                        hostel.addmalemember(fellow)
                else:
                    break
            self.occupied_hostels.append(hostel)
            if len(self.people['fellows']) == 0:
                break

    def allocated_members_list(self):

        '''Method used to show alloation list. '''

        for room in self.occupied_offices:
            print "For the {} Office those allocated are: " .format(room.name)
            if room.roommembers:
                for i, value in enumerate(room.roommembers):
                    print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
            else:
                    print ('No Allocation to this room.')
            print("" * 1)


        for room in self.occupied_hostels:
            if room.type == 'm':
                print 'For {} Male room those allocated are:'.format(room.name)
                if room.malemember:
                    for i, value in enumerate(room.malemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
                else:
                    print ('No Allocation to this room.')
                print("" * 1)

        for room in self.occupied_hostels:
            if room.type == 'f':
                print 'For {} Female room those allocated are:'.format(room.name)
                if room.femalemember:
                    for i, value in enumerate(room.femalemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
                else:
                    print ('No Allocation to this room.')
                print("" * 1)



    def unallocated_members_list(self):

        '''Method used to show unallocated list '''

        print ('List of Unallocated fellows to Rooms')

        if len(self.people['fellows']):
            for i, value in enumerate(self.people['fellows']):
                print i+1, value.name, value.position, value.gender
            print("" * 1)
        else:
            if len(self.people['fellows']) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
            print ("" * 1)

        print ('List of Unallocated office Members.')
        if len(self.people['everyone']):
            for i, value in enumerate(self.people['everyone']):
                print i+1, value.name, value.position, value.gender
        else:
            if len(self.people['everyone']) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)


    def maleroom_members(self, rooms):

        '''Method used to get members assigned to specific room  
        Usage: Building.maleroom_members('opal').
        '''

        for room in self.occupied_hostels:
            if room.type == 'm' and room.name == rooms :
                print "For the {} maleroom those allocated are: " .format(room.name)
                for i, value in enumerate(room.malemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
                print("" * 1)


    def femaleroom_members(self, rooms):

        '''Method used to get members assigned to specific room  
            Usage: Building.femaleroom_members('ruby').
        '''

        for room in self.occupied_hostels:
            if room.type == 'f':
                if room.name == rooms :
                    print "For the {} femaleroom those allocated are: " .format(room.name)
                    for i, value in enumerate(room.femalemember):
                        if room.femalemember:
                            print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
                        else:
                            print "No one present in this room."
                    print("" * 1)


    def officeroom_members(self, rooms):

        '''Method used to get members assigned to specific room  
            Usage: Building.officeroom_members('Mint').
        '''

        for offices in self.occupied_offices:
            if offices.name == rooms:
                print "For the {} office those allocated are: " .format(offices.name)
                for i, value in enumerate(offices.roommembers):
                    if offices.roommembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value.name, value.position, value.gender)
                    else:
                        print "No one present in this room."
                print("" * 1)





