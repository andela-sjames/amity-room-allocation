'''Script use to view result of allocation.'''
from building import Building, people
from parser import Parser

people = Parser.read_file('input2.txt')

Building.populateroom()
Building.allocate_to_office()
Building.allocate_to_livingspace()
Building.allocated_members_list()
Building.Unallocated_member_list()
Building.maleroom_members('topaz')
Building.femaleroom_members('pearl')
Building.officeroom_members('Vulcan')




