'''This script reads data from the '.txt' file and stores them into different containers.'''


import re
import random


class GetData(object):

    """Class definition used to get data from input.txt. 
    
    Data read from file is randomly shuffled here for random allocation.
    """
    
    def __init__(self):
        self.input = 'input.txt'
    
    def read_file(self):

        '''Method returns the text file data and saves in list. '''        
        
        data = []
        with open(self.input, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for inputdata in inputfile:
                inputdata = inputdata.strip('\n')
                part = entry.search(inputdata)
                dataset = part.groups()
                dataset = list(dataset)
                data.append(dataset,)
                random.shuffle(data)


            return data

    def officedata(self):

        ''' Method returns a total number contained in textfile. '''

        return self.read_file()

    def maledata(self):

        ''' Method returns data for male fellows that applied. '''

        maledatarecord = []
        with open(self.input, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for maledata in inputfile:
                maledata = maledata.strip('\n')
                part = entry.search(maledata)
                maleset = part.groups()
                maleset = list(maleset)
                if maleset[1] == 'M' and maleset[2] == "FELLOW" and maleset[3] == 'Y':
                    maledatarecord.append(maleset)
                    random.shuffle(maledatarecord)
                
            return maledatarecord

    def femaledata(self):

        '''Method returns data for female fellows that applied. '''

        femaledatarecord = []
        with open(self.input, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for femaledata in inputfile:
                femaledata = femaledata.strip('\n')
                part = entry.search(femaledata)
                femaleset = part.groups()
                femaleset = list(femaleset)
                if femaleset[1] == 'F' and femaleset[2] == "FELLOW" and femaleset[3] == 'Y':
                    femaledatarecord.append(femaleset)
                    random.shuffle(femaledatarecord)

            return femaledatarecord

    def notallocated_tolivingspacedata(self):

        ''' Method returns data for fellows that didn't apply. '''

        natls = []
        with open(self.input, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for natlsdata in inputfile:
                natlsdata = natlsdata.strip('\n')
                part = entry.search(natlsdata)
                natlsset = part.groups()
                natlsset = list(natlsset)
                if natlsset[2] == 'FELLOW' and natlsset[3] == 'N':
                    natls.append(natlsset)
                    random.shuffle(natls)


            return natls

    def staff_not_allocated_to_rooms(self):

        ''' Method returns data of staff containaed in text file. '''

        snatr = []
        with open(self.input, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w+)\s(\w)?')
            for snatrdata in inputfile:
                snatrdata = snatrdata.strip('\n')
                part = entry.search(snatrdata)
                snatrset = part.groups()
                snatrset = list(snatrset)
                if snatrset[3] == None:
                    snatr.append(snatrset)
                    random.shuffle(snatr)


            return snatr
            