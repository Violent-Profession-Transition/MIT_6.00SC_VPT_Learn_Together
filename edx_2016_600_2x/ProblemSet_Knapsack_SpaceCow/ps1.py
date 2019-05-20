###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Parameters:
    filename - the name of the data file as a string
    Returns:
    a dictionary of cow name (string), weight (int) pairs
    {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    """
    cow_dict = dict()
    f = open(filename, 'r')
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # trips is a list of list
    trips = []
    num_trips = 0
    # flattern the cows_dict
    cows_list = []
    for cow in cows:
        cow_name = cow
        cow_weight = cows[cow]
        cows_list.append([cow_name, cow_weight])
    # cows_list is now
    # [['Callie', 2], ['Jesse', 6], ['Maggie', 5], ['Maybel', 3]]
    # sort the cows_list by weight
    sorted_cows = sorted(
        cows_list,
        key=lambda x: x[1],
        reverse=True)
    while len(sorted_cows) > 0:
        # remaining cows
        remaining_cows = sorted_cows[:]
        #  print("remaining_cows is: ", remaining_cows)
        # for each trip, use greedy by weight
        tot_weight = 0
        trip = []
        for cow in remaining_cows:
            #  print("trying out cow: ", cow)
            if tot_weight + cow[1] <= limit:
                #  print("can board cow ", cow)
                trip.append(cow[0])
                tot_weight += cow[1]
                # pop the cow from sorted_cows
                sorted_cows.remove(cow)
        # add the trip to the trips
        trips.append(trip)
        num_trips += 1
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # construct the list of cows' names for partition set
    cows_names = []
    for cow in cows:
        cows_names.append(cow)
    #print("all the cows names in a list: ", cows_names)
    # for all the possible trips
    min_num_trips = len(cows_names)
    #print("minimum num of trips: ", len(cows_names))
    best_trips = None
    for trips in get_partitions(cows_names):
        #print("now try out trips: ", trips)
        invalid_trips = False
        # trips = [['Callie', 'Jesse'], ['Maybel', 'Maggie']]
        for trip in trips:
            w_trip = 0
            # trip = ['Callie', 'Jesse']
            for cow in trip:
                # cow = 'Callie'
                w_trip += cows[cow]
            #print("total weight of ", trip, " is: ", w_trip)
            if w_trip > limit:
                # if the weight of any of the
                # trip in the trips is
                # bigger than limit
                # discard the trips
                invalid_trips = True
                #print("trips is invalid! skip this trips")
                break
            #print("trip is ok")
        if invalid_trips:
            continue
        # calculate the num of trips
        num_trips = len(trips)
        if num_trips <= min_num_trips:
            min_num_trips = num_trips
            best_trips = trips
    return best_trips


#cows = load_cows("ps1_cow_data.txt")
#limit=100
cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
limit = 10

#print(greedy_cow_transport(cows, limit))
# [["Jesse", "Maybel"], ["Maggie", "Callie"]]

#print(greedy_cow_transport({'Muscles': 65, 'Horns': 50, 'Milkshake': 75, 'MooMoo': 85, 'Patches': 60, 'Clover': 5, 'Polaris': 20, 'Louis': 45, 'Lotus': 10, 'Miss Bella': 15}, 100))
# [['MooMoo', 'Miss Bella'], ['Milkshake', 'Polaris', 'Clover'], ['Muscles', 'Lotus'], ['Patches'], ['Horns', 'Louis']]

#print(greedy_cow_transport({'Coco': 10, 'Rose': 50, 'Patches': 12, 'Buttercup': 72, 'Dottie': 85, 'Abby': 38, 'Daisy': 50, 'Lilly': 24, 'Betsy': 65, 'Willow': 35}, 100))
# [['Dottie', 'Patches'], ['Buttercup', 'Lilly'], ['Betsy', 'Willow'], ['Daisy', 'Rose'], ['Abby', 'Coco']]

#print(greedy_cow_transport({'Coco': 59, 'Buttercup': 11, 'Abby': 28, 'Rose': 42, 'Luna': 41, 'Betsy': 39, 'Starlight': 54, 'Willow': 59}, 120))
# [['Willow', 'Coco'], ['Starlight', 'Rose', 'Buttercup'], ['Luna', 'Betsy', 'Abby']]


#  print(brute_force_cow_transport(cows, limit))
#print(brute_force_cow_transport({'Betsy': 65, 'Buttercup': 72, 'Daisy': 50}, 75))
# [['Daisy'], ['Betsy'], ['Buttercup']]

#print(brute_force_cow_transport({'Boo': 20, 'Milkshake': 40, 'Horns': 25, 'Lotus': 40, 'MooMoo': 50, 'Miss Bella': 25}, 100))
# [['Lotus', 'Milkshake', 'Boo'], ['MooMoo', 'Horns', 'Miss Bella']]

test_cow_1 = {'Boo': 20, 'Milkshake': 40, 'Horns': 25, 'Lotus': 40, 'MooMoo': 50, 'Miss Bella': 25}
test_limit_1 = 100

print(greedy_cow_transport(test_cow_1, test_limit_1))
print(brute_force_cow_transport(test_cow_1, test_limit_1))
