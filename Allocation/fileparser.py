'''This script reads data from the '.txt' file and stores them into different containers.'''


import re
import random
from persons import Fellow, Staff, Person

class Parser(object):

    """Class definition gets data from inputfile. 
    Uses input.txt as default if none specified.
    """

    @staticmethod
    def read_file(filename = 'input.txt'):

        '''Method returns the text file data and saves in Classes Instance. '''             
        people = {
            'staff': [],
            'fellows': [],
            'everyone': [],
        }
        with open(filename, 'r') as inputfile:
            entry = re.compile(r'(\w+\s[^\s]+)\s{0,}(\w)\s{0,}(\w+)(\s\w)?')
            for inputdata in inputfile:
                inputdata = inputdata.strip('\n')
                part = entry.search(inputdata)
                line = part.groups()
                line = list(line)
                if line:
                    person = Person(line[0], line[1], line[2])
                    people['everyone'].append(person)

                if line[2] == 'FELLOW':
                    wants_living = True if line[3].strip()  == 'Y' else False
                    person = Fellow(line[0], line[1], line[2], wants_living)
                    people['fellows'].append(person)
                else:
                    person = Staff(line[0], line[1], line[2])
                    people['staff'].append(person)

        return people

        

        