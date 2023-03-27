from test_data import testing_data, testing_error_data

"""
Received email on Monday 27th 2:15PM
Started at 14:45PM

Step 1: Create a function that takes two inputs: 
    Array of integers
    Integer to represent taps
Function should return the total number of seconds that it takes for all people to have filled their water bottles.
Assume that once a tap is free it next peson uses that tapp immiedetly and cannot move to a different tap once they started filling
Each tap flows at a rate of 100ml per second (e.g 1 litre bottle takes 10 seconds)

Finished inital function 16:36PM
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


"""
Conceived a more efficent way of coming up with the correct answer based on looking at the test data

Instead of creating two arrays that would add to each other, one array is only needed and we just need to count how much time each array was being used for.
Then we find the max and that is how long it takes for each bottle to be filled

Finished inital function 17:07pm
"""
def FillUpBottleVersionTwo(water_bottles, taps):
    taps = [0] * taps
    water_bottles = [bottle / 100 for bottle in water_bottles]
    for bottle in water_bottles:
        taps[taps.index(min(taps))] += bottle
    return max(taps)


"""
Step two:
Adding in data validation, we want to return an error if the data is invalid and explain why.
"""
def ValidateData(input_data):
    if len(input_data) == 1:
        if isinstance(input_data[0], list):
            raise Exception("Please enter how many taps are being used at the festival")
        raise Exception("Please enter the amount of water bottles needed to be filled")
    try:
        FillUpBottleVersionTwo(input_data[0], input_data[1])
    except IndexError:
        print("Error: Missing either ")
    except Exception as e:
        print(e.__class__.__name__)
    


if __name__ == "__main__":
    """
    for data in testing_data:
        print(FillUpBottle(data[0], data[1]))
        print(FillUpBottleVersionTwo(data[0], data[1]))
    """
    for data in testing_error_data:
        print(ValidateData(data))