####[![Coverage Status](https://coveralls.io/repos/andela-sjames/RandomSpaceAllocation/badge.svg?branch=master&service=github)](https://coveralls.io/github/andela-sjames/RandomSpaceAllocation?branch=master)

# RandomSpaceAllocation

#####Just as the name implies this short Algorithm was created to randomly allocate company members to randomly generated rooms.

Within the Scope of these algorithm the code has a pre-defined number of offices for allocation and a predefined number of hostels to allocate to male and female fellows who opted for it. This definition can be found in the `Rooms.py` file. You can always modified that after you fork this repo.

```
Algorithm  Basic Conditions are:

1. No staff should be allocated to Male or Female Rooms
2. No Male or Female room should exceed 4 persons
3. No office allocation should exceed 6 persons

```

######The input into this Script can be found in the input.txt file where the input format can be viewed or seen below:

```
BOLA AHMED   M FELLOW Y
JOHN OBI     M FELLOW N
ISSAC NNADI  M STAFF   
CRIBS JANE   F FELLOW Y
```

The above input format specifies the Name of the Company's member, the member's gender, the member's position and the member's choice. One more thing here, Staffs are not allocated to either male or female offices and so they have no choice to make from the sample data input.

###Work Flow

The `readfile.py` reads data and stores them  in different containers according to the conditions given, then randomly shuffled them for random allocation.

The `rooms.py` stores the class definition, pre-defined offices, male and females rooms to be allocated at run time.

The `Allocate.py` makes use of the data returned from the `readfile.py` script and the class definitions and rooms definition found in the `rooms.py` script. The `Allocate.py` script allocates based on conditions given ensuring that each room meets desired condition before allocating to the next room. ofcourse no one knows who is going to be placed in any room because everything is random and there is no certainty. 

The `viewresult.py` outputs your result in details.

###To use Script 

Give Script input data following the ```sample input.txt``` given above and you can add rooms to rooms.py.

Run command `python viewresult.py` and your result will be displayed for you. 

###Have fun!!!!!




