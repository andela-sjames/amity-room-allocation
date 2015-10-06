'''This script reads data from the '.txt' file and stores them into different containers.'''


import re
import random

filename = 'input.txt'

class GetData(object):

    """Class definition used to get data from inputfile. 
    Uses input.txt as default if none specified.
    Data read from file is randomly shuffled here for random allocation.
    """

    @staticmethod
    def read_file(filename = 'input.txt'):

        '''Method returns the text file data and saves in list. '''        
        
        data = []
        with open(filename, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for inputdata in inputfile:
                inputdata = inputdata.strip('\n')
                part = entry.search(inputdata)
                dataset = part.groups()
                dataset = list(dataset)
                data.append(dataset,)
                random.shuffle(data)


            return data


    @staticmethod
    def generatedata():

        '''Method returns sorted data and saves in different list. '''

        maledatarecord = []
        femaledatarecord = []
        notallocatedtolivingspace = []
        staffnotallocatedtorooms = []
        officedatarecord = GetData.read_file(filename)[:]
        for value in officedatarecord:
            if value[1] == 'M' and value[2] == "FELLOW" and value[3] == 'Y':
                maledatarecord.append(value)
                random.shuffle(maledatarecord)

            if value[1] == 'F' and value[2] == "FELLOW" and value[3] == 'Y':
                    femaledatarecord.append(value)
                    random.shuffle(femaledatarecord)

            if value[2] == 'FELLOW' and value[3] == 'N':
                notallocatedtolivingspace.append(value)
                random.shuffle(notallocatedtolivingspace)

            if value[3] == None:
                staffnotallocatedtorooms.append(value)
                random.shuffle(staffnotallocatedtorooms)

        return maledatarecord, femaledatarecord, notallocatedtolivingspace, staffnotallocatedtorooms

        


        