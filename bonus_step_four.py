original_testing_data = [400, 750, 1000] 
extended_original_testing_data = [400, 750, 1000, 300, 750, 2000]

large_amount_bottle_data = [
            5300, 1600, 3200, 5600, 2900, 600, 9800, 4700, 8500, 700, 6300, 3900, 5900, 
            2700, 5200, 3700, 3500, 9100, 1600, 7900, 5900, 8800, 6900, 9200, 24200
]

small_amount_bottle_data = [
    100, 300, 400, 600
]

very_big_bottles_data = [
    500000, 50000, 50000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 500000, 5000000
]

five_bottle_data = [
    100, 100, 100, 500, 1000
]

fibonacci_bottle_data = [100, 200]

for i in range(1, 10):
    fibonacci_bottle_data.append((fibonacci_bottle_data[i-1] + fibonacci_bottle_data[i]))

final_massive_bottle = [
    200, 200, 200, 200, 200, 100, 50, 20000
]

alternating_bottles = [
    200, 100, 200, 100, 200, 100
]

alternating_bottles_with_a_large_bottle = [
    200, 100, 200, 100, 200, 100, 200, 100, 200, 1000, 100, 200, 100, 10000
]

first_tap_reach_largest_bottle_data = [
    100, 200, 200, 100, 200, 200, 100, 200, 300, 100000, 200, 300, 100, 100, 100, 100, 100
]


all_testing_data = [
    original_testing_data, extended_original_testing_data,
    large_amount_bottle_data, small_amount_bottle_data,
    very_big_bottles_data, five_bottle_data,
    fibonacci_bottle_data, final_massive_bottle, 
    alternating_bottles, alternating_bottles_with_a_large_bottle, 
    first_tap_reach_largest_bottle_data,
]


def DifferentTapSpeedFillUp(water_bottles, taps):
    time_at_taps = [0] * len(taps)
    for bottle in water_bottles:
        free_tap = time_at_taps.index(min(time_at_taps))
        time_at_taps[free_tap] += ((bottle / taps[free_tap]) + 3)
    return max(time_at_taps)

def CreateFile(name, start_point):
    f = open(name, 'w+')
    for data in all_testing_data:
        f.write(f"Data Used: {data}\n")
        slowest_time = 0
        times = []
        for i in range(start_point, 30):
            faster_tap = 100 + (int(i) * 10)
            current_time = DifferentTapSpeedFillUp(data, [100, faster_tap])
            times.append(current_time)
            text_to_write = f"[100, {faster_tap}] speed of taps. "
            if current_time > slowest_time:
                slowest_time = current_time
                text_to_write += f"Time taken: {current_time} - New Slowest Time\n"
            else:
                text_to_write += f"Time taken: {current_time}\n"
            f.write(text_to_write)
        f.write(f"final slowest time:      {slowest_time}\n")
    f.close()

"""
Bonus Step 4 result summary:

My main result from performing this data test is the following.

If both taps start at the same rate: Increasing one of the taps start rate will always be faster or same time as the result of both taps at the same speed.

However, if both taps start at different rates, you can potentially line up with a slower time by making one of the taps faster, I have found this out using the
data set final_massive_bottle and alternating_bottles_with_a_large_bottle. From what I have gathered with these two data points is that it is possible for a 
faster tap rate to have a longer time needed for filling all bottles, if the staps are not equal to start with and for the slower tap to get the largest bottle.
"""
if __name__ == "__main__":
    CreateFile('same_tap_speed_start_result.txt', 0)
    CreateFile('different_tap_speed_start_result.txt', 1)
