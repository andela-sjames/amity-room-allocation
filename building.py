'''This script uses data from the rooms.py file and readfile.py to allocate.'''

from parser import Parser
from rooms import Office, LivingSpace
import random

people = Parser.read_file()
occupied_offices =[]
occupied_hostels = []
room_directory = {
            'offices': [],
            'livingspaceroom': [],
            }


class Building(object):

    @staticmethod
    def populateroom():

        offices = ['Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge', 'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan',]

        malerooms = [('m','topaz'), ('m','silver'), ('m','gold'), ('m','onyx'), ('m','opal'),]

        femalerooms = [('f','ruby'), ('f','platinum'), ('f','jade'), ('f','pearl'), ('f','diamond'),]


        for room_name in offices:
            room_directory['offices'].append(room_name)

        for room_name in malerooms:
            room_directory['livingspaceroom'].append(room_name)

        for room_name in femalerooms:
            room_directory['livingspaceroom'].append(room_name)      

        return room_directory

    @staticmethod
    def space_data(space):
        
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

        officedata = []
        livingspacedata = []
        #femaledata = []

        for space in room_directory:
            if space == room:
                for office_name in room_directory[space]:
                    officedata.append(office_name)
                return officedata

            if space == room:
                for roomname in room_directory[space]:
                    livingspacedata.append(roomname)
                return livingspacedata


    @staticmethod
    def allocate_to_office():

        officedataset = Building.space_data('everyone')
        random.shuffle(officedataset)
        for office_name in Building.get_room_list('offices'):            
            office = Office(office_name)
            while len(office.roommembers) < office.maxpersons:
                position = officedataset.pop()
                office.addmember(position)
            occupied_offices.append(office)
            if len(Building.space_data('everyone')) == 0:
                break

        return officedataset

    @staticmethod
    def allocate_to_livingspace():
        fellowdataset = Building.space_data('fellows')
        random.shuffle(fellowdataset)
        for hostelname in Building.get_room_list('livingspaceroom'):
            hostel = LivingSpace(hostelname[0],hostelname[1])
            while len(hostel.femalemember) < hostel.maxpersons and len(hostel.malemember) < hostel.maxpersons:
                if len(fellowdataset):
                    position = fellowdataset.pop()
                    if position[1] == 'F' and position[3]:
                        hostel.addfemalemember(position)

                    if position[1] == 'M' and position[3]:
                        hostel.addmalemember(position)
                else:
                    break
            occupied_hostels.append(hostel)
            if len(Building.space_data('fellows')) == 0:
                break


        return fellowdataset

    @staticmethod
    def allocated_members_list():
        for room in occupied_offices:
            print "For the {} Office those allocated are: " .format(room.name)
            if room.roommembers:
                for i, value in enumerate(room.roommembers):
                    print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
            else:
                    print ('No Allocation to this room.')
            print("" * 1)


        for room in occupied_hostels:
            if room.type == 'm':
                print 'For {} Male room those allocated are:'.format(room.name)
                if room.malemember:
                    for i, value in enumerate(room.malemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                else:
                    print ('No Allocation to this room.')
                print("" * 1)

        for room in occupied_hostels:
            if room.type == 'f':
                print 'For {} Female room those allocated are:'.format(room.name)
                if room.femalemember:
                    for i, value in enumerate(room.femalemember):
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                else:
                    print ('No Allocation to this room.')
                print("" * 1)



    @staticmethod
    def Unallocated_member_list():

        print ('List of Unallocated fellows to Rooms')

        if len(Building.allocate_to_livingspace()):
            for i, value in enumerate(Building.allocate_to_livingspace()):
                print i+1, value[0], value[2], value[1]
            print("" * 1)
        else:
            if len(Building.allocate_to_livingspace()) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
            print ("" * 1)

        print ('List of Unallocated office Members.')
        if len(Building.allocate_to_office()):
            for i, value in enumerate(Building.allocate_to_office()):
                print i+1, value[0], value[2], value[1]
        else:
            if len(Building.allocate_to_office()) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print("" * 1)


    @staticmethod
    def maleroom_members(rooms):
        for room in occupied_hostels:
            if room.type == 'm':
                if room.name == rooms :
                    print "For the {} maleroom those allocated are: " .format(room.name)
                    for i, value in enumerate(room.malemember):
                        if room.malemember:
                            print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                        else:
                            print "No one present in this room."
                    print("" * 1)



    @staticmethod
    def femaleroom_members(rooms):
        for room in occupied_hostels:
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
        for offices in occupied_offices:
            if offices.name == rooms:
                print "For the {} office those allocated are: " .format(offices.name)
                for i, value in enumerate(offices.roommembers):
                    if offices.roommembers:
                        print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                    else:
                        print "No one present in this room."
                print("" * 1)




