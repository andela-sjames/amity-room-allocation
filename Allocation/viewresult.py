'''Script use to view result of allocation.'''
from building import Building, people
from fileparser import Parser

Building.populateroom()
Building.allocate_to_office()
Building.allocate_to_livingspace()
Building.allocated_members_list()
Building.unallocated_members_list()

Building.maleroom_members('opal')
Building.femaleroom_members('ruby')
Building.officeroom_members('Mint')

#input .txt file from building.py
#Usage: people = Parser.read_file('your .txt file here.')
