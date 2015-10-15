'''This script uses data from the persons.py file and rooms.py to allocate.'''

from fileparser import Parser
from rooms import Office, LivingSpace
import random

people = Parser.read_file('input.txt')

class Directory(object):

    ''' Class defined to store office and livingspace data.'''

    occupied_offices =[]
    occupied_hostels = []
    office_memberA = []
    the_fellowsB = []
    room_directory = {
        'offices': [],
        'livingspaceroom': [],
        }


class Building(object):

    '''Class mimics an actual building and contains methods to view result. '''

    @staticmethod
    def populateroom():

        offices = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge', 'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan',]

        livingspacerooms = [('m','topaz'), ('m','silver'), ('m','gold'), ('m','onyx'), ('m','opal'),('f','ruby'), ('f','platinum'), ('f','jade'), ('f','pearl'), ('f','diamond'),]

        for room_name in offices:
            Directory.room_directory['offices'].append(room_name)

        for room_name in livingspacerooms:
            Directory.room_directory['livingspaceroom'].append(room_name)

        return Directory.room_directory

    @staticmethod
    def space_data(space):

        '''Method used to get data from class instances of persons.py '''
        
        office_data = []
        living_data = []
        staff_data = []
        for data in people:
            if data == space:
                for individual in people[data]:
                    office_data.append([individual.name, individual.gender, individual.position,individual.wants_living])
                return office_data

            if data == space:
                for individual in people[data]:
                    living_data.append([individual.name, individual.gender, individual.position, individual.wants_living])
                return living_data

            if data == space:
                for individual in people[data]:
                    staff_data.append([individual.name, individual.gender, individual.position, individual.wants_living])
                return staff_data
        
    @staticmethod
    def get_room_list(room):

        '''Method used by allocate method to get room list specified.'''

        officedata = []
        livingspacedata = []

        for space in Directory.room_directory:
            if space == room:
                for office_name in Directory.room_directory[space]:
                    officedata.append(office_name)
                return officedata

            if space == room:
                for roomname in Directory.room_directory[space]:
                    livingspacedata.append(roomname)
                return livingspacedata


    @staticmethod
    def allocate_to_office():

        '''Method used to allocate members to offices. ''' 

        office_member = Building.space_data('everyone')
        random.shuffle(office_member)
        for office_name in Building.get_room_list('offices'):            
            office = Office(office_name)
            while len(office.roommembers) < office.maxpersons:
                if len(office_member):
                    position = office_member.pop()
                    office.addmember(position)
                else:
                    break
            Directory.occupied_offices.append(office)
            if len(Building.space_data('everyone')) == 0:
                break

        for data in office_member:
            Directory.office_memberA.append(data)


    @staticmethod
    def allocate_to_livingspace():

        ''' Method used to allocate fellows to rooms.'''

        the_fellows = Building.space_data('fellows')
        random.shuffle(the_fellows)
        for hostelname in Building.get_room_list('livingspaceroom'):
            hostel = LivingSpace(hostelname[0],hostelname[1])
            while len(hostel.femalemember) < hostel.maxpersons and len(hostel.malemember) < hostel.maxpersons:
                if len(the_fellows):
                    position = the_fellows.pop()
                    if position[1] == 'F' and position[3]:
                        hostel.addfemalemember(position)

                    if position[1] == 'M' and position[3]:
                        hostel.addmalemember(position)
                else:
                    break
            Directory.occupied_hostels.append(hostel)
            if len(Building.space_data('fellows')) == 0:
                break


        for data in the_fellows:
            Directory.the_fellowsB.append(data)

    @staticmethod
    def allocated_members_list():

        '''Method used to show alloation list. '''

        for room in Directory.occupied_offices:
            print "For the {} Office those allocated are: " .format(room.name)
            if room.roommembers:
                for i, value in enumerate(room.roommembers):
                    print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
            else:
                    print ('No Allocation to this room.')
            print("" * 1)


        for room in Directory.occupied_hostels:
            if room.type == 'm':
                print 'For {} Male room those allocated are:'.format(room.name)
                if room.malemember:
                    for i, value in enumerate(room.malemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                else:
                    print ('No Allocation to this room.')
                print("" * 1)

        for room in Directory.occupied_hostels:
            if room.type == 'f':
                print 'For {} Female room those allocated are:'.format(room.name)
                if room.femalemember:
                    for i, value in enumerate(room.femalemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                else:
                    print ('No Allocation to this room.')
                print("" * 1)



    @staticmethod
    def unallocated_members_list():

        '''Method used to show unallocated list '''

        print ('List of Unallocated fellows to Rooms')

        if len(Directory.the_fellowsB):
            for i, value in enumerate(Directory.the_fellowsB):
                print i+1, value[0], value[2], value[1]
            print("" * 1)
        else:
            if len(Directory.the_fellowsB) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
            print ("" * 1)

        print ('List of Unallocated office Members.')
        if len(Directory.office_memberA):
            for i, value in enumerate(Directory.office_memberA):
                print i+1, value[0], value[2], value[1]
        else:
            if len(Directory.office_memberA) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)


    @staticmethod
    def maleroom_members(rooms):

        '''Method used to get members assigned to specific room  
        Usage: Building.maleroom_members('opal').
        '''


        for room in Directory.occupied_hostels:
            if room.type == 'm' and room.name == rooms :
                print "For the {} maleroom those allocated are: " .format(room.name)
                for i, value in enumerate(room.malemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                print("" * 1)



    @staticmethod
    def femaleroom_members(rooms):

        '''Method used to get members assigned to specific room  
            Usage: Building.femaleroom_members('ruby').
        '''

        for room in Directory.occupied_hostels:
            if room.type == 'f':
                if room.name == rooms :
                    print "For the {} femaleroom those allocated are: " .format(room.name)
                    for i, value in enumerate(room.femalemember):
                        if room.femalemember:
                            print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                        else:
                            print "No one present in this room."
                    print("" * 1)


    @staticmethod
    def officeroom_members(rooms):

        '''Method used to get members assigned to specific room  
            Usage: Building.officeroom_members('Mint').
        '''

        for offices in Directory.occupied_offices:
            if offices.name == rooms:
                print "For the {} office those allocated are: " .format(offices.name)
                for i, value in enumerate(offices.roommembers):
                    if offices.roommembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                    else:
                        print "No one present in this room."
                print("" * 1)





