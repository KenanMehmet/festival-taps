from test_data import (
    testing_data, testing_error_data, 
    different_flow_rates_testing_data, different_flow_rates_testing_error_data
)

"""
Received email on Monday 27th 14:15
Started at 14:45

Initial Problem: Create a function that takes two inputs: 
    Array of integers
    Integer to represent taps
Function should return the total number of seconds that it takes for all people to have filled their water bottles.
Assume that once a tap is free it next peson uses that tapp immiedetly and cannot move to a different tap once they started filling
Each tap flows at a rate of 100ml per second (e.g 1 litre bottle takes 10 seconds)

Finished inital function 16:36
"""

def FillUpBottle(water_bottles, taps):
    """
    To find how long to it takes to fill a water bottle we will take the bottle amount and divide it by the tap_fill_rate 
    This is because the bottles and tap rate is measured in 100ml

    Initally had tap_fill_rate as a variable but taken away as it was only used in one area
    """
    taps = [0] * taps # create an array of each tap, this record seconds being used by each tap
    occupied_taps = taps.copy() # copy the above array, this will be used to count how many seconds each tap will be used for.
    water_bottles = [bottle / 100 for bottle in water_bottles] #find how many seconds each bottle will take to fill
    for bottle in water_bottles:
        if 0 not in occupied_taps: # if there any free taps
            minimum_time = min(occupied_taps) # Save minimum time here 
            taps = list(map(lambda num: num + minimum_time, taps)) #Run a function over each tap, this function adds the minimum time to each entry
            occupied_taps = list(map(lambda num: num - minimum_time, occupied_taps)) #Same as the above but we reduce the time.
        occupied_taps[occupied_taps.index(0)] += bottle #Find an unoccupied tap and add how long it will take to fill up that bottle to 
    return max([taps[i] + occupied_taps[i] for i in range(0, len(taps))])


"""
Conceived a more efficent way of coming up with the correct answer based on looking at the test data

Instead of creating two arrays that would add to each other, one array is only needed and we just need to count how much time each tap was being used for.
Then we find the max time a tap was used for, this represents how long it takes for all bottles to be filled, as the max time will be the last bottle
being filled up.

Finished inital function 17:07
"""
def FillUpBottleVersionTwo(water_bottles, taps):
    taps = [0] * taps
    water_bottles = [bottle / 100 for bottle in water_bottles]
    for bottle in water_bottles:
        taps[taps.index(min(taps))] += bottle # Find the current lowest value tap, and add the time it takes to fill up the bottle to the tap
    return max(taps)


"""
Bonus Step One:
Adding in data validation, we want to return an error if the data is invalid and explain why.

Types of incorrect data.

Float decimals
Empty lists
Strings in the list of water bottles
String for the tap
Lists for taps
Dictionaries
Class Objects
"""
def ValidateData(input_data):
    error = ""
    if len(input_data) == 2:
        if isinstance(input_data[0], list):
            if len(input_data[0]) > 0:
                bottles = input_data[0]
                taps = input_data[1]
                try:
                    return(FillUpBottleVersionTwo(bottles, int(taps)))
                except TypeError:
                    if any(str(bottle) == bottle for bottle in bottles):
                        error +="Type Error: You have entered a string for a water bottle\n"
                    if not isinstance(bottles, list):
                        error +="Type Error: Please enter a list for the water bottles to be filled up\n"
                except ValueError:
                    if taps == str(taps):
                        error +="Value Error: A string was entered for the amount of taps\n"
            else:
                error +="Input Error: You have entered an empty list for the water bottles needed to be filled up\n"
        else:
            if type(input_data[0]) != list:
                error += "Input Error: The water bottles input is not in a list format\n"
            if type(input_data) != int:
                error += "Input Error: The taps input is not an integer\n"
    else:
        if len(input_data) > 2:
            error +="Error: You have inputed too many variables, this function takes a list variable, and an integer.\n"
        if isinstance(input_data[0], list):
            error +="Error: Please enter how many taps are being used at the festival\n"
        else:
            error +=("Error: Please enter the water bottles needed to be filled\n")
    error += "Please try again\n"
    return error
    
"""
Bonus Step Two:
Time to walk to tap:

We will now no longer assume that the tap once its free will be instantly used by another person.
We will now assume that it will take an extra fixed amount of time for each person to walk from the queue to the tap,
For this version we will assume that it will take an extra 3 seconds to walk to the tap, we have the first person for each tap
start with this extra 3 seconds as well.
"""

def WalkToTap(water_bottles, taps):
    taps = [0] * taps
    water_bottles = [bottle / 100 for bottle in water_bottles]
    for bottle in water_bottles:
        taps[taps.index(min(taps))] += (bottle + 3) # we will add on an extra 3 seconds to represent someone walking to the tap.
    return max(taps)

"""
Bonus Step Three
Different Flow of taps:

We have initally assumed that the taps will all be running at the same speed, now we will assume that each
tap will have a different ml per second, e.g tap 1 will be at 100ml per second and tap 2 will be at 200 ml per second.

Changes that we will be making to our test data is converting the integer to representing taps into a list which 
will hold the speed of each tap in ml

I will experiement with different ways of modeling this data:

1) Model the tap array the same as before but instead use the taps positional variable to calculate time

2) The tap array will now hold arrays which include time at tap and the tap flow speed

3) Two different arrays, one to hold the time spent at the taps, another being the flow rate

Went with the first model as it was the most efficient way of modeling that data
"""

def DifferentTapSpeedFillUp(water_bottles, taps):
    time_at_taps = [0] * len(taps)
    for bottle in water_bottles:
        free_tap = time_at_taps.index(min(time_at_taps))
        time_at_taps[free_tap] += ((bottle / taps[free_tap]) + 3)
    return max(time_at_taps)

"""
I will also update the ValidateData function to include this new change to the taps.
"""

def ValidateFlowRateData(input_data):
    error = ""
    if len(input_data) == 2:
        if isinstance(input_data[0], list) and isinstance(input_data[1], list):
            if len(input_data[0]) > 0 and len(input_data[1]) > 0:
                bottles = input_data[0]
                taps = input_data[1]
                try:
                    return(FillUpBottleVersionTwo(bottles, int(taps)))
                except TypeError:
                    if any(str(bottle) == bottle for bottle in bottles):
                        error +=("Type Error: One of the waterbottles in your list is a string and not an integer\n")
                    if not isinstance(bottles, list):
                        error +=("Type Error: Please enter a list for the water bottles to be filled up\n")
                    if not isinstance(taps, list):
                        error +=("Type Error: Please enter a list for the water bottles to be filled up\n")
                    if any(str(tap) == tap for tap in taps):
                        error +=("Type Error: One of the taps flow rate in your list is a string and not an integer\n")
                except ValueError:
                    if taps == str(taps):
                        error +=("Value Error: A string was entered for the amount of taps\n")
            else:
                if len(input_data[0]) == 0:
                    error +=("Error: You have entered an empty list for the water bottles needed to be filled up\n")
                if len(input_data[1]) == 0:
                    error +=("Error: You have entered an empty list for the tap flow rate needed to be filled up\n")
        else:
            if type(input_data[0]) != list:
                error += "Input Error: The water bottles input is not in a list format\n"
            if type(input_data[1]) != list:
                error += "Input Error: The taps input is not in a list format\n"
    else:
        if len(input_data) > 2:
            error +=("Error: You have inputed an extra field to consider, this function takes two seperate lists\n")
        else:
            error +=("Error: Please enter the flow rate of the taps at the festival.\n")
    error += "Please try again\n"
    return error


if __name__ == "__main__":

    """
    Here will the data from the inital function will be ran,
    I have included both the original function and my updated function to show that they reach the same result.
    """
    for data in testing_data:
        print(FillUpBottle(data[0], data[1]))
        print(FillUpBottleVersionTwo(data[0], data[1]))

    """
    Here we will run the testing data
    """
    for data in testing_error_data:
        print(ValidateData(data))

    """
    Here we will be running the function where we check the extra time it takes to walk to the tap
    """
    for data in testing_data:
        print(WalkToTap(data[0], data[1]))

    """
    Here we will run the function for different tap speeds
    """
    for data in different_flow_rates_testing_data:
        print(DifferentTapSpeedFillUp(data[0], data[1]))

    for data in different_flow_rates_testing_error_data:
        print(ValidateFlowRateData(data))