'''Script use to view result of allocation.'''

from Allocate import Allocate, GetData, occupied_offices, officedata, unplacedofficedata, occupied_malerooms, maledata, unplacedfemaledata, unplacedmaledata, occupied_femalerooms, femaledata

start = Allocate()
start.allocate_office()
start.allocate_malerooms()
start.allocate_femalerooms()
fromfile = GetData()
Natls = fromfile.notallocated_tolivingspacedata()
Snatr = fromfile.staff_not_allocated_to_rooms()


class ViewResults(object):

    ''' Class defined to view results of allocation. '''

    def print_result(self):

        '''Method prints desired results.'''

        print "AMITY OFFICE AND MEMBERS ASSIGNED. "
        for room in occupied_offices:
            print "For the {} Office those allocated are: " .format(room.name)
            for i, value in enumerate(room.officemembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])

            print

        print "Out of a total of {} members, {} members where allcated while {} members where not allocated." .format(len(officedata), (len(officedata) - len(unplacedofficedata)), len(unplacedofficedata))
        print
        print "Allocated persons to office are {}" .format(len(officedata) - len(unplacedofficedata))
        print

        if len(unplacedofficedata):
            print "You can view the {} unallocated members below." .format(len(unplacedofficedata))
            for i, value in enumerate(unplacedofficedata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedofficedata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print


        #Maleroom allocation view point.

        print "AMITY MALEROOMS AND MEMBERS ASSIGNED. "
        for room in occupied_malerooms:
            print "For the {} maleroom those allocated are: " .format(room.name)
            for i, value in enumerate(room.maleroommembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])
                print

        print "Out of a total of {} members, {} members applied for male living space. But only {} males where allocated. " .format(len(officedata), len(maledata), (len(maledata)-len(unplacedmaledata)))
        print
        print "Allocated members to malerooms are {}" .format(len(maledata)-len(unplacedmaledata))
        print

        if len(unplacedmaledata):
            print "You can view the {} unallocated members below." .format(len(unplacedmaledata))
            for i, value in enumerate(unplacedmaledata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedmaledata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print



        # Femaleroom allocation view point.

        print "AMITY FEMALEROOMS AND MEMBERS ASSIGNED. "
        for room in occupied_femalerooms:
            print "For the {} femaleroom those allocated are: " .format(room.name)
            for i, value in enumerate(room.femaleroommembers):
                print "{}. {} a {}. Gender:{}  " .format(i+1, value[0], value[2], value[1])

            print

        print "Out of a total of {} members, {} members applied for female living space. But only {} females where allocated. " .format(len(officedata), len(femaledata), (len(femaledata)-len(unplacedfemaledata)))
        print
        print "Allocated members to femalerooms are {}" .format(len(maledata)-len(unplacedmaledata))
        print

        if len(unplacedfemaledata):
            print "You can view the {} unallocated members below." .format(len(unplacedfemaledata))
            for i, value in enumerate(unplacedfemaledata):
                print i+1, value[0], value[2], value[1]
        else:
            if len(unplacedfemaledata) == 0:
                print "EVERYONE WAS ALLOCATED BOSS"
        print

        #Summary Report Section.

        print "SUMMARY REPORT BOSS "
        print "Out of a Total of {}, {} fellows where not allocated to either male or female rooms because there didn't opt for it. {} staffs were not also allocated to living sapces because staffs are not required to apply for living space. {} female members applied for female living space while {} male members applied for male living space. That's the whole Truth, Nothing but the truth boss. " .format(len(officedata), len(Natls), len(Snatr), len(femaledata), len(maledata))

results = ViewResults()
results.print_result()
