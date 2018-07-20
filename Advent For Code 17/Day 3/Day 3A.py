END_STOP = 500

import math

# Square all odd numbers between 1 and END_STOP
ls = [math.pow(x,2) for x in list(range(1,END_STOP)) if x % 2 == 1]

# Loop through, look for value closest to 312051
for ls in ls:
    print("")
# Then break when you've got the closest one.

# Use your defined find function to find the distance from the corner to the value you're looking for.

def find(corner_value, search_value):
    pass
