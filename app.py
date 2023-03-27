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
    taps = [0] * taps # create an array of each ta, this record seconds being used by each tap
    occupied_taps = taps.copy() # copy the above array, this will be used to count how many seconds each tap will be used for.
    water_bottles = [bottle / 100 for bottle in water_bottles] #find how many seconds each bottle will take to fill
    for bottle in water_bottles:
        if 0 not in occupied_taps:
            minimum_time = min(occupied_taps) # Save minimum time here 
            taps = list(map(lambda num: num + minimum_time, taps)) #Run a function over each tap, this function adds the minimum time to each entry
            occupied_taps = list(map(lambda num: num - minimum_time, occupied_taps)) #Same as the above but we reduce the time.
        occupied_taps[occupied_taps.index(0)] += bottle #Find an unoccupied tap and add how long it will take to fill up that bottle to 
    return max([taps[i] + occupied_taps[i] for i in range(0, len(taps))])

def FillUpBottleVersionTwo(water_bottles, taps):
    taps = [0] * taps
    water_bottles = [bottle / 100 for bottle in water_bottles]
    for bottle in water_bottles:
        taps[taps.index(min(taps))] += bottle
    return max(taps)

if __name__ == "__main__":
    for data in testing_data:
        print(FillUpBottle(data[0], data[1]))
        print(FillUpBottleVersionTwo(data[0], data[1]))