'''Unittest Script to check code fuctionality.'''

from fileparser import Parser 
from building import Building
from rooms import Office, LivingSpace

import unittest

class TestParserClass(unittest.TestCase):

    '''Class used to test if .txt file is read.'''

    def setUp(self):
        self.parse = Parser()

    def test_data_is_readfrom_inputfile(self):

        '''Test that read_file method returns a not null value'''
        
        self.assertIsNotNone(self.parse.read_file('input.txt'), msg='Parser.rea_file should not return an empty value ')

class TestBuildingClass(unittest.TestCase):

    '''Class used to test builing is populated and allocates rooms.'''

    def setUp(self):
        self.build = Building()

    def test_building_is_populated_with_data(self):

        self.assertIsNotNone(self.build.populateroom(), msg ='room_directory should be poplated with data from list.')

        self.assertIsNotNone(self.build.space_data('everyone'), msg ='data from returned parser class should be callable')

        self.assertIsNotNone(self.build.get_room_list('offices'), msg ='list of offices available should be returned')

        self.assertIsNotNone(self.build.get_room_list('livingspaceroom'), msg = 'list of livingspace room should be returned')

    def test_data_allocation_function_returns_None(self):

        self.assertIsNone(self.build.allocate_to_livingspace(), msg='method should not return any value')

        self.assertIsNone(self.build.allocate_to_office(), msg='method should return any value')

    def test_data_is_printed(self):

        self.assertIsNone(self.build.allocated_members_list(), msg = 'method should print data and not return a value.')

        self.assertIsNone(self.build.unallocated_members_list(), msg = 'method should print data and not return a value.')

        self.assertIsNone(self.build.maleroom_members('opal'),msg ='should print data and not return a value')

        self.assertIsNone(self.build.femaleroom_members('ruby'),msg ='should print data and not return a value')

        self.assertIsNone(self.build.officeroom_members('Mint'),msg ='should print data and not return a value')


class TestRoomsClass(unittest.TestCase):

    def setUp(self):
        self.office = Office('Vulcan')
        self.livingspace = LivingSpace('m', 'topaz')

    def test_class_instance_created(self):
        self.assertIsInstance(
            self.office, Office,
            msg="office should be an instance of 'Office' class")

        self.assertIsInstance(
            self.livingspace, LivingSpace,
            msg="livingspace should be an instance of 'LivingSpace' class")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
