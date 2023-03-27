from test_data import testing_data


"""
Received email on Monday 27th 2:15PM
Started at 14:45PM

Step 1: Create a function that takes two inputs: 
    Array of integers
    Integer to represent taps
Function should return the total number of seconds that it takes for all people to have filled their water bottles.
Assume that once a tap is free it next peson uses that tapp immiedetly and cannot move to a different tap once they started filling
Each tap flows at a rate of 100ml per second (e.g 1 litre bottle takes 10 seconds)

basic flowchart.

if free tap:
    go to tap

"""

tap_fill_rate = 100

def FillUpBottle(water_bottles, taps):
    """
    To find how long to it takes to fill a water bottle we will take the bottle amount and divide it by the tap_fill_rate 
    This is because the bottles and tap rate is measured in 100ml
    """
    taps = [0 for tap in range(0, taps)]
    occupied_taps = taps.copy()
    water_bottles = [x / 100 for x in water_bottles]

    #seconds = 0
    print("starting")
    for bottle in water_bottles:
        print(occupied_taps)
        for i in range(0, len(occupied_taps)):
            print(occupied_taps.index(i))
            if occupied_taps[i] == 0:
                print(occupied_taps[i])
                occupied_taps[i] += bottle
                break
            if 0 not in occupied_taps:
                print(0 not in occupied_taps)
                PassTime(taps)
        print(taps, occupied_taps)
    seconds = sum(taps)
    return seconds

def PassTime(taps, occupied_taps):
    print(taps, occupied_taps)
    minimum_time = occupied_taps.min()
    print(minimum_time)
    for tap in taps:
        tap += minimum_time[1]
        occupied_taps -= minimum_time
    print(taps)
    print(occupied_taps)
        



#print(FillUpBottle(testing_data[0][0], testing_data[0][1]))
print(FillUpBottle(testing_data[0][0], 2))