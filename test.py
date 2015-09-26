'''Unittest Script to check code fuctionality.'''

from readfile import GetData
from viewresult  import ViewResults
from rooms import OfficeRoom, LivingSpacesMale, LivingSpacesFemale, amityfemalerooms, amitymalerooms, amityoffices
from Allocate import Allocate, unplacedofficedata, unplacedmaledata, unplacedfemaledata, occupied_femalerooms, occupied_malerooms, occupied_offices
import unittest


class TestGetData(unittest.TestCase):

    '''Class used to test if .txt file is read.'''

    def setUp(self):
        self.get = GetData()

    def test_read_file(self):
        '''Test read_file method is called.'''
        self.assertIsNotNone(self.get.read_file(), msg="a valid set of data is  called")

    def test_officedata_is_returned(self):
        '''Test that length of data is same from read_file method.'''
        self.assertEqual(len(self.get.officedata()), len(self.get.read_file()), msg="files should not be altered")

    def test_data_input(self):
        '''Test that officedata exist.'''
        self.assertIsNotNone(self.get.officedata(), msg="a valid set of item should be returned")

    def test_maledata_function(self):
        '''Test that maledata returned is not none.'''
        self.assertIsNotNone(self.get.maledata(), msg="a valid set of item should be returned")

    def test_femaledata_function(self):
        '''Test that femaledata returned is not None.'''
        self.assertIsNotNone(self.get.femaledata(), msg="a valid set of item should be returned")

    def test_natls_function(self):
        '''Test that NOT allocated data is returned.'''
        self.assertIsNotNone(self.get.notallocated_tolivingspacedata(), msg="a valid set of item should be returned")

    def test_snatr_function_is_called(self):
        '''Test that staff not allocated data is returned.'''
        self.assertIsNotNone(self.get.staff_not_allocated_to_rooms(), msg="a valid set of item should be returned")

class TestAllocate(unittest.TestCase):

    '''Test that data is properly allocated.'''

    def setUp(self):
        self.allocate = Allocate()
        self.officeroom = OfficeRoom('office')
        self.livingspacemale = LivingSpacesMale('maleroom')
        self.livingspacefemale = LivingSpacesFemale('femaleroom')

    def test_allocate_rooms(self):
        '''Test that room instances are created.'''
        self.assertIsInstance(
            self.officeroom, OfficeRoom,
            msg="officeroom should be an instance of 'OfficeRoom' class")

        self.assertIsInstance(
            self.livingspacemale, LivingSpacesMale,
            msg="livingspacemale should be an instance of 'LivingSpacesMale' class")

        self.assertIsInstance(
            self.livingspacefemale, LivingSpacesFemale,
            msg="livingspacefemale should be an instance of 'LivingSpacesFemale' class")

    def test_office_appended(self):
        '''Test that office are populated.'''
        for office in amityoffices:
            officeroom = OfficeRoom(office)
            while len(officeroom.officemembers) < officeroom.maxofficepersons:
                self.assertLess(len(officeroom.officemembers), officeroom.maxofficepersons, msg="number must not exceed condition set")
                if len(unplacedofficedata):
                    position = unplacedofficedata.pop()
                    officeroom.addofficemember(position)
                else:
                    break
            occupied_offices.append(officeroom)
            self.assertIn(officeroom, occupied_offices, msg="officeroom names should be appended to list")
            if len(unplacedofficedata) == 0:
                break

    def test_maleroom_appended(self):
        '''Test that male rooms are populated.'''
        for maleroom in amitymalerooms:
            livingspacemale = LivingSpacesMale(maleroom)
            while len(livingspacemale.maleroommembers) < livingspacemale.maxmalepersons:
                if len(unplacedmaledata):
                    position = unplacedmaledata.pop()
                    livingspacemale.addmalemembers(position)
                else:
                    break
            occupied_malerooms.append(livingspacemale)
            self.assertIn(livingspacemale, occupied_malerooms, msg=" maleroom names should be appended to list")
            if len(unplacedmaledata) == 0:
                break


    def test_femaleroom_appended(self):
        '''Test that female rooms are populated.'''
        for femaleroom in amityfemalerooms:
            livingspacefemale = LivingSpacesFemale(femaleroom)
            while len(livingspacefemale.femaleroommembers) < livingspacefemale.maxfemalepersons:
                if len(unplacedfemaledata):
                    position = unplacedfemaledata.pop()
                    livingspacefemale.addfemalemember(position)
                else:
                    break
            occupied_femalerooms.append(livingspacefemale)
            self.assertIn(livingspacefemale, occupied_femalerooms, msg=" femaleroom names should be appended to list")
            if len(unplacedfemaledata) == 0:
                break


class Printdata(unittest.TestCase):

    '''Class to check data is printed.'''

    def setUp(self):
        self.getresult = ViewResults()


    def data_is_printed(self):
        '''Test that results are printed.'''
        self.assertIsNotNone(self.getresult.print_result(), msg="all results should be printed")






if __name__ == '__main__':
    unittest.main(verbosity=2)
    