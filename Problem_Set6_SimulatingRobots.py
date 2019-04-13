#!/usr/bin/python2

"""
design a simulation and implement a program that uses classes
Roomba vacuuming robot
design a simulation to estimate how much time a group of Rommba
robots will take to clean the floor of a room
"""

"""
robots are points, can pass through each other
and occupy the same point
Position class to represent coordinates
speed is 's', every time-step robot moves in direction by
s units
Tiles: (0,0), (0,1), ... (0, h-1),...
the simulation terminates when a specified fraction of the
tiles in the room are cleaned
"""
import random
import math
import matplotlib.pyplot as plt

import ps6_visualize

# === Provided classes

class Position:
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)
    def __str__(self):
        return "Position ({},{})".format(self.x, self.y)

# === Problems 1
# Two classes for
# Rectangular room &
# Robot
class RectangularRoom:
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        # construct a list of all tiles
        all_tiles = []
        for w in range(width):
            for h in range(height):
                all_tiles.append((w,h))
        # Initially, no tiles in the room have been cleaned
        self.all_tiles = all_tiles
        self.clean_tiles = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position Object
        """
        tile_x, tile_y = pos.getX(), pos.getY()
        # if tile is clean, do not mark it again
        tile_x, tile_y = int(math.floor(tile_x)), int(math.floor(tile_y))
        if (tile_x,tile_y) not in self.clean_tiles:
            self.clean_tiles.append((tile_x, tile_y))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m,n) in self.clean_tiles:
            return True
        return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        return len(self.clean_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        w = random.random() * self.width
        h = random.random() * self.height
        return Position(round(w,1), round(h,1))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # cannot be negative pos
        if pos.getX() < 0 or pos.getY() < 0:
            return False
        elif pos.getX() > self.width or pos.getY() > self.height:
            return False
        else:
            return True

    def __str__(self):
        return "Rectangular Room width: {} height: {}".format(self.width, self.height)

class Robot:
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        pos = room.getRandomPosition()
        self.pos = pos
        # random direction
        direction = random.randint(0,359)
        self.direction = direction
        # speed
        self.speed = speed

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        return self.pos

    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # mark the tile it is on as clean
        self.room.cleanTileAtPosition(self.pos)
        # move to a new position
        self.pos = self.pos.getNewPosition(self.direction, self.speed)

    def __str__(self):
        return "Robot @ position {} with direction {} and speed of {}".format(self.pos, self.direction, self.speed)


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.
    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # mark the tile it is on as clean
        self.room.cleanTileAtPosition(self.pos)
        # try move to a new position
        # print("trying moving now ~")
        new_pos = self.pos.getNewPosition(self.direction, self.speed)
        # if NOT hit a wall:
        if self.room.isPositionInRoom(new_pos):
            self.pos = new_pos
            # and update the cleaned tiles
            self.room.cleanTileAtPosition(self.pos)
            # print("moved to new tile and cleaned!")
        else:
            # print("will hit a wall! stop and turn...")
            # will hit a wall, so only change direction
            # random direction
            while True:
                new_direction = random.randint(0,359)
                if new_direction != self.direction:
                    break
            self.direction = new_direction

# === Problem 3

def runSimulation(num_robots=1, speed=1, width=5, height=5, min_coverage=1, num_trials=1, robot_type=StandardRobot, use_tk=True):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    #print("##### Start simulations #####")
    # run trials
    total = 0
    for t in range(num_trials):
        #print("===== trail {} =====".format(t))
        count = run_trial(num_robots, width, height, min_coverage, robot_type, speed, use_tk)
        #print("trail {} takes {} clock ticks to clean the room of {}x{} for {} coverage".format(t, count, width, height, min_coverage))
        total += count
    # calculate the average
    avg = float(total) / num_trials
    print("avg is: ", avg)
    return avg


def room_cleaned(room, min_coverage):
    """check if the room's clean tiles have reached min coverage"""
    return (room.getNumCleanedTiles()/float(room.getNumTiles())) >= min_coverage

def run_trial(num_robots, width, height, min_coverage, robot_type, speed, use_tk):
    """a single trial of simulation
    return number of clock ticks to clean > min_coverage
    """
    # instantiate a room
    room = RectangularRoom(width, height)
    # print(room)
    # instantiate robot list
    robots = []
    for i in range(num_robots):
        robot = robot_type(room, speed)
        # print("created a robot:")
        # print(robot)
        robots.append(robot)
    # count the clock ticks
    count = 0
    if use_tk:
        # init the visualization
        anim = ps6_visualize.RobotVisualization(num_robots, width, height, delay=.01)
    # terminate when room is clean
    while not room_cleaned(room, min_coverage):
        # print("clock tick>>>")
        count += 1
        # clean the room
        for robot in robots:
            # print(robot)
            robot.updatePositionAndClean()
        if use_tk:
            # update the tk window after delay
            anim.update(room, robots)
    if use_tk:
        # stop tk
        anim.done()
    return count

# test runSimulation()
runSimulation(use_tk=False)
runSimulation(width=10,height=10,min_coverage=0.75)
runSimulation(width=20,height=20)


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of
    cleaning time on number of robots.
    """
    plt.figure(1) # 1st figure
    plt.title("How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?")
    # x is num of robots
    plt.xlabel("Number of robots")
    x = list(range(1,11))
    # y is clock ticks
    plt.ylabel("Clock ticks to clean room")
    y = []
    trials=20
    for num_robot in range(1,11):
        avg = runSimulation(num_robots=num_robot,width=20,height=20,min_coverage=0.8,num_trials=trials,use_tk=False)
        y.append(avg)
    plt.plot(x,y,'ro')
    plt.text(5,400,"Number of Trials: {}".format(trials))
    plt.show()

# showPlot1()


def showPlot2():
    """
    Produces a plot showing dependence of
    cleaning time on room shape.
    """
    plt.figure(2) # 2nd figure
    plt.title("two robots to clean rooms of various shapes for 80% coverage")
    # x is num of robots
    plt.xlabel("Room Shape")
    dimensions = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    x = []
    for d in dimensions:
        pair = "{}x{}".format(d[0],d[1])
        x.append(pair)
    # y is clock ticks
    plt.ylabel("Clock ticks to clean room")
    y = []
    trials=20
    for d in dimensions:
        avg = runSimulation(num_robots=2,width=d[0],height=d[1],min_coverage=0.8,num_trials=trials,use_tk=False)
        y.append(avg)
    print(x,y)
    plt.plot(list(range(6)),y,'ro')
    plt.text(3,600,"Number of Trials: {}".format(trials))
    plt.show()

# showPlot2()

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # mark the tile it is on as clean
        self.room.cleanTileAtPosition(self.pos)
        # print(self)
        # try move to a new position
        # with a random direction
        # print("trying moving now ~")
        new_direction = random.randint(0,359)
        self.setRobotDirection(new_direction)
        # print("random walk----")
        new_pos = self.pos.getNewPosition(self.direction, self.speed)
        # if NOT hit a wall:
        if self.room.isPositionInRoom(new_pos):
            self.pos = new_pos
            # and update the cleaned tiles
            self.room.cleanTileAtPosition(self.pos)
            # print(self)
            # print("moved to new tile and cleaned!")
        else:
            # print("will hit a wall! stop and turn...")
            # will hit a wall, so only change direction
            # random direction
            while True:
                new_direction = random.randint(0,359)
                if new_direction != self.direction:
                    break
            self.setRobotDirection(new_direction)

# test runSimulation() using RandomWalkRobot
runSimulation(robot_type=RandomWalkRobot)
runSimulation(width=10,height=10,min_coverage=0.75,robot_type=RandomWalkRobot)
runSimulation(width=20,height=20,robot_type=RandomWalkRobot)

# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    plt.figure(3) # 3rd figure
    plt.title("Straight-line Robot vs Random-Walk Robot")
    # x is room size for square rooms
    plt.xlabel("Room Size")
    x = [a**2 for a in range(10,31,10)]
    # y_straight is clock ticks for straight line robot
    plt.ylabel("Clock ticks to clean room")
    y_straight = []
    trials=10
    for i in range(10,31,10):
        avg = runSimulation(num_robots=1,width=i,height=i,min_coverage=0.8,num_trials=trials,use_tk=False)
        y_straight.append(avg)
    # y_rw is clock ticks for random walk robot
    y_rw = []
    for i in range(10,31,10):
        avg = runSimulation(num_robots=1,width=i,height=i,min_coverage=0.8,num_trials=trials,robot_type=RandomWalkRobot,use_tk=False)
        y_rw.append(avg)
    print(x,y_rw)
    plt.plot(x,y_straight,'bo', x,y_rw,'ro')
    plt.text(3,600,"Number of Trials: {}".format(trials))
    plt.show()

# showPlot3()

def showPlot4():
    """
    Produces a plot showing dependence of
    cleaning time on number of robots.
    """
    plt.figure(4)
    plt.title("How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?")
    # x is num of robots
    plt.xlabel("Number of robots")
    x = list(range(1,11))
    # y is clock ticks
    plt.ylabel("Clock ticks to clean room")
    y = []
    z = []
    trials=20
    for num_robot in range(1,11):
        avg_s = runSimulation(num_robots=num_robot,width=20,height=20,min_coverage=0.8,num_trials=trials,use_tk=False)
        y.append(avg_s)
        avg_r = runSimulation(num_robots=num_robot,width=20,height=20,min_coverage=0.8,num_trials=trials,robot_type=RandomWalkRobot,use_tk=False)
        z.append(avg_r)
    print(x,y,z)
    plt.plot(x,y,'ro', x,z,'bo')
    plt.legend(('StandardRobot', 'RandomWalkRobot'))
    plt.text(5,400,"Number of Trials: {}".format(trials))
    plt.show()

showPlot4()

def showPlot5():
    """
    Produces a plot showing dependence of
    cleaning time on room shape.
    """
    plt.figure(5)
    plt.title("two robots to clean rooms of various shapes for 80% coverage")
    # x is num of robots
    plt.xlabel("Room Shape")
    aspect_ratios = []

    # y and z is clock ticks
    plt.ylabel("Clock ticks to clean room")
    y = []
    z = []
    trials=200
    for width in [10, 20, 25, 50]:
        height = 300/width
        aspect_ratios.append(float(width) / height)
        avg_s = runSimulation(num_robots=2,width=width,height=height,min_coverage=0.8,num_trials=trials,use_tk=False)
        y.append(avg_s)
        avg_r = runSimulation(num_robots=2,width=width,height=height,min_coverage=0.8,num_trials=trials,robot_type=RandomWalkRobot,use_tk=False)
        z.append(avg_r)
    print(aspect_ratios,y,z)
    plt.plot(aspect_ratios,y,'ro',aspect_ratios,z,'bo')
    plt.legend(('StandardRobot', 'RandomWalkRobot'))
    plt.text(3,600,"Number of Trials: {}".format(trials))
    plt.show()

showPlot5()