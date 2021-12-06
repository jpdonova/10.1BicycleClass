"""
Joe Donovan
Assignment: 10.1 Your Own Class
Description: Create your own class with a demo program. I created a bicycle class that takes in the number of gears the
bicycle has and a name. Several class variables are derived from the number of gears inputted. There are functions
to increase the speed, acceleration and gear you are on under different conditions, along with just getting the info
"""


# imports random for use in main() function
import random


# my custom class represents a bicycle
class Bicycle:
    # private class variable that holds the number of wheels for a bicycle
    __number_of_wheels = 2

    # constructor class that takes in a name and the number of gears the bike, from which a bunch of other instance
    # variables are derived from
    def __init__(self, name, num_gears):
        # try catch to make sure name and num_gears can be a string and an int respectively
        try:
            # casts name as a string and sets it to a private instance variable
            self.__name = str(name)

            # if statement to test if num_gears is either greater than or equal to 7 or 1
            if num_gears >= 7 or num_gears == 1:
                self.__num_gears = int(num_gears)
            # otherwise just sets it equal to 7
            else:
                self.__num_gears = 7
            # sets an instance variable to hold the current gear of the bike which is 1
            self.__current_gear = 1

            # if statement set instance variable to different values depending on the instance variable __num_gears
            # if __num_gears is 7 then you make the max speed equal to 21
            if 7 == self.__num_gears:
                self.__max_speed = self.__num_gears * 3
            # if the __num_gears is 1
            elif self.__num_gears == 1:
                # sets __max_speed to 20
                self.__max_speed = 20
            # if __num_gears is in between 7 and 24, sets the max speed to the __num_gears times 2.5
            elif 24 > self.__num_gears > 7:
                self.__max_speed = self.__num_gears * 2.5
            # if the amount of gears is more than 24, then its sets __max_speed to 28
            else:
                self.__max_speed = 28

            # if statement to set a __max_acceleration instance variable based on __num_gears
            if self.__num_gears == 1:
                # if the number of gears is 1 private instance variable __max_acceleration is set to 5
                self.__max_acceleration = 5
            elif 7 >= self.__num_gears > 1:
                # if the number of gears is 7 private instance variable __max_acceleration is set to 5
                self.__max_acceleration = 6
            elif 24 > self.__num_gears > 7:
                # if the number of gears is between 7 and 24 private instance variable __max_acceleration is set to 5
                self.__max_acceleration = self.__num_gears/3
            else:
                # if the number of gears is more than 24 private instance variable __max_acceleration is set to 5
                self.__max_acceleration = 6

            #  __acceleration represents the current acceleration which is used to increase the speed of the bike
            # it is based on the current gear and total number of gears
            # and multiplies that ratio by the max acceleration
            self.__acceleration = (self.__current_gear / self.__num_gears) * self.__max_acceleration
            # sets the current start speed to 0
            self.__current_speed = 0
            # excepts value error if name cant be a string and if num_gears cant be an int
        except ValueError:
            # creates a bike with one gear and default values of that bike
            print("The first argument has to be a string and the other four have to be ints! Created a default bicycle")
            self.__name = "default_name"
            self.__num_gears = 1
            self.__current_gear = 1
            self.__max_speed = 20
            self.__max_acceleration = 5
            self.__acceleration = 0
            self.__current_speed = 0

    # getter function for private instance variable name, returns name
    def get_name(self):
        return self.__name

    # setter function for private instance variable name, returns new name, returns none if argument cant be a string
    def set_name(self, name):
        # try except value error in case argument cant become a string
        try:
            self.__name = str(name)
            return self.__name
        except ValueError:
            # prints error message
            print("argument has to be able to become a string")
            # returns none
            return None

    # getter for private instance variable __num_gears, returns __num_gears
    def get_gears(self):
        return self.__num_gears

    # getter for private instance variable __max_speed, returns __max_speed
    def get_max_speed(self):
        return self.__max_speed

    # setter for __num_gears, takes in an int as an argument, has helper functions to update things based on the new
    # self.__num_gears
    def set_num_of_gears(self, gears):
        # try except value error in case argument cant become an int
        try:
            self.__num_gears = int(gears)
            # helper functions that are private that update the values of __max_acceleration, _max_speed, and
            # __update_acceleration which are all reliant on the __num_gears
            self.__update_max_acceleration()
            self.__update_max_speed()
            self.__update_acceleration()
            self.__current_gear = 1
            self.__current_speed = 0
            return self.__num_gears
        # excepts value error
        except ValueError:
            # prints error message
            print("argument has to be able to become a string")
            # returns none
            return None

    # function to replicate the creation of __max_acceleration that is in the constructor
    # this is a helper function for the set_num_of_gears function
    def __update_max_acceleration(self):
        if self.__num_gears == 1:
            # if the number of gears is 1 private instance variable __max_acceleration is set to 5
            self.__max_acceleration = 5
        elif 7 >= self.__num_gears > 1:
            # if the number of gears is 7 private instance variable __max_acceleration is set to 5
            self.__max_acceleration = 6
        elif 24 > self.__num_gears > 7:
            # if the number of gears is between 7 and 24 private instance variable __max_acceleration is set to 5
            self.__max_acceleration = self.__num_gears / 3
        else:
            # if the number of gears is more than 24 private instance variable __max_acceleration is set to 5
            self.__max_acceleration = 6
        return self.__max_acceleration

    # function to replicate the creation of __acceleration that is in the constructor
    # this is a helper function for the set_num_of_gears function
    def __update_acceleration(self):
        #  __acceleration represents the current acceleration which is used to increase the speed of the bike
        # it is based on the current gear and total number of gears
        # and multiplies that ratio by the max acceleration
        self.__acceleration = (self.__current_gear / self.__num_gears) * self.__max_acceleration
        return self.__acceleration

    # function to replicate the creation of __max_speed that is in the constructor
    # this is a helper function for the set_num_of_gears function
    def __update_max_speed(self):
        if 7 == self.__num_gears:
            self.__max_speed = self.__num_gears * 3
        # if the __num_gears is 1
        elif self.__num_gears == 1:
            # sets __max_speed to 20
            self.__max_speed = 20
        # if __num_gears is in between 7 and 24, sets the max speed to the __num_gears times 2.5
        elif 24 > self.__num_gears > 7:
            self.__max_speed = self.__num_gears * 2.5
        # if the amount of gears is more than 24, then its sets __max_speed to 28
        else:
            self.__max_speed = 28
        return self.__max_speed

    # getter function for __current_speed private instance variable
    def get_speed(self):
        return self.__current_speed

    # getter function for __number_of_wheels private class variable
    def get_number_of_wheels(self):
        return self.__number_of_wheels

    # getter function to get the current acceleration, returns private class variable self.__acceleration
    def get_acceleration(self):
        return self.__acceleration

    # getter function to get the current gear, returns private class variable self.__current_gear
    def get_current_gear(self):
        return self.__current_gear

    # function for changing the gear either up or down one depending on direction argument, has to be either + or -
    def change_gear(self, direction):
        # if isinstance to check if direction is a string
        if isinstance(direction, str):
            if direction == "+":
                # if to make sure the current gear cant go above the number of gears
                if self.__current_gear < self.__num_gears:
                    self.__current_gear += 1
                    # updates the acceleration, reliant of the current gear
                    self.__update_acceleration()
                    return self.__current_gear
                else:
                    pass
            elif direction == "-":
                # if to make sure the gear doesnt drop down to 0
                if self.__current_gear > 1:
                    self.__current_gear -= 1
                    # updates the acceleration, reliant of the current gear
                    self.__update_acceleration()
                    return self.__current_gear
                else:
                    pass
            # else if direction isnt either + or -
            else:
                print("The string argument has to be either a '+' or a '-' ")
                # returns original __current_gear
                return self.__current_gear
        # else if direction isnt a string
        else:
            print("The argument has to be a string that is either '+' or '-' ")
            # returns original __current_gear
            return self.__current_gear

    # function to increase the speed of the bike
    def increase_speed(self):
        # if statement to control the amount the speed is increasing
        # if the current speed is less than the max speed - max acceleration, increases __current_speed by the acceleration,
        # this adds the most out of the other conditional
        if self.__current_speed < self.__max_speed - self.__max_acceleration:
            self.__current_speed += self.__acceleration
        elif self.__current_speed > self.__max_speed - self.__max_acceleration:
            self.__current_speed += self.__acceleration/2
        # if statement if the current speed goes over the maximum speed, prints message, and sets the current speed to max
        if self.__max_speed < self.__current_speed:
            print("speed can't increase any further")
            self.__current_speed = self.__max_speed
        # returns the new current speed
        return self.__current_speed


# demo code! Simulates a race and prints different information about the bikes with the getter functions
def main():
    # creates three bikes that fill self.__name self.__num_gears self.__max_speed self.__max_acceleration
    #  and self.__current_speed based on the number of gears inputted.
    bike1 = Bicycle("Joe's Bike", 21)
    bike2 = Bicycle("Bob's Bike", 12)
    bike3 = Bicycle("Billy's Bike", 24)
    # creates an array of bikes
    bikes = [bike1, bike2, bike3]
    # creates an array of ints that hold the positions of the bikes
    bike_positions = [0, 0, 0]
    # loops over the bikes and prints different info using the getters of the private variables
    for bike in bikes:
        # f string to allow getter functions to be cast as strings and concatenated automatically
        print(f"{bike.get_name()}: Speed:{bike.get_speed()} Gear: {bike.get_current_gear()} Acceleration: {bike.get_acceleration()}")
    # print to show the start of the race of the three bikes
    print("Start race.")
    # temp variable to hold the first place position, used to know when race ends with the while loop
    first_place_position = 0
    # while loop to last the length of the race until someone passes the finish line
    while first_place_position < 10:
        counter = 0
        for bike in bikes:
            options = ["+", "-"]
            bike.change_gear(random.choice(options))
            bike.increase_speed()
            bike_positions[counter] += bike.get_speed()
            counter += 1
        for num in bike_positions:
            if num > first_place_position:
                first_place_position = num
            else:
                pass
        # end of for loop, updates first_place_position
    # end of while loop
    # prints bikes array at bike_positions's index of first_place_position the first place positions
    # so the bike who one, which the name is gotten with get_name
    print(f"{bikes[bike_positions.index(first_place_position)].get_name()} won the race!")
    # for loop to print finished state of the bikes
    for bike in bikes:
        print(f"{bike.get_name()}: Speed:{bike.get_speed()} Gear: {bike.get_current_gear()} Acceleration: {bike.get_acceleration()}")


# if statement to run main
if __name__ == '__main__':
    main()
