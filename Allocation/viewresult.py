'''Script use to view result of allocation.'''
from building import Building
from fileparser import Parser

amity = Building('input.txt');
amity.populate_rooms()
amity.allocate_to_office()
amity.allocate_to_livingspace()
amity.allocated_members_list()
amity.unallocated_members_list()

amity.maleroom_members('opal')
amity.femaleroom_members('ruby')
amity.officeroom_members('Mint')