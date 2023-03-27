testing_data = [
    [
        [
            400, 750, 1000
        ], 
        [100, 100]
    ],
    [
        [
            400, 750, 1000
        ], 
        [100, 200]
    ],
    [
        [
            400, 750, 1000
        ], 
        [100, 250]
    ],
    [
        [
            400, 750, 1000
        ], 
        [100, 500]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 100]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 110]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 120]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 130]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 110]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 200]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 300]
    ],
    [
        [
            400, 750, 1000, 300, 750, 2000 
        ],
        [100, 500]
    ]
]

testing_bottle_data = [
            5300, 1600, 3200, 5600, 2900, 600, 9800, 4700, 8500, 700, 6300, 3900, 5900, 
            2700, 5200, 3700, 3500, 9100, 1600, 7900, 5900, 8800, 6900, 9200, 24200
]

secondary_bottle_data = [
    100, 300, 400, 600
]

very_big_bottle_data = [
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

first_tap_reach_largest_bottle_data = [
    100, 200, 200, 100, 200, 200, 100, 200, 300, 100000, 200, 300, 100, 100, 100, 100, 100
]

small_amount_data = [
    100, 100, 200, 300, 400, 500
]


def DifferentTapSpeedFillUp(water_bottles, taps):
    time_at_taps = [0] * len(taps)
    for bottle in water_bottles:
        free_tap = time_at_taps.index(min(time_at_taps))
        time_at_taps[free_tap] += ((bottle / taps[free_tap]) + 3)
    return max(time_at_taps)

if __name__ == "__main__":
    """
    slowest_time = 0
    times = []
    for i in range(1, 100):
        faster_tap = 100 + (int(i) * 10)
        current_time = DifferentTapSpeedFillUp(final_massive_bottle, [100, faster_tap])
        times.append(current_time)
        if current_time > slowest_time:
            print("New slower time")
            print([100, faster_tap])
            print(current_time)
            slowest_time = current_time
    print(times)
    """
    slowest_time = 0
    times = []
    for i in range(1, 100):
        faster_tap = 100 + (int(i) * 10)
        current_time = DifferentTapSpeedFillUp(very_big_bottle_data, [faster_tap, 100])
        times.append(current_time)
        if current_time > slowest_time:
            print("New slower time")
            print([100, faster_tap])
            print(current_time)
            slowest_time = current_time
    print(times)