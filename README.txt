Git Hub Repo: https://github.com/jpdonova/10.1BicycleClass

Joe Donovan
Assignment: 10.1 Your Own Class, README.txt file
Description: Create your own class with a demo program. I created a bicycle class that takes in the number of gears the
bicycle has and a name. Several class variables are derived from the number of gears inputted. There are functions
to increase the speed, acceleration and gear you are on under different conditions, along with just getting the info

This class represents a bicycle.
There are a total of 7 instance variables:
    self.__name - This variable holds the name of the bicycle in an instance variable for identification of the bike. This value is stored as a string, and has a setter and a getter.
    self.__num_gears - This variable hold the total number of gears in a given bicycle object. This variable is used to create self.__max_speed and self.__max_acceleration in the constructor. The two functions __update_max_acceleration and __update_max_speed mimic the creation of those tow variable based on this variable when self.__num_gears is updated.
    self.__max_speed - This variable holds the maximum speed of the bike. This variable is created from the self.__num_gears variable and is used to create and update the self.__current_speed variable.
    self.__max_acceleration This variable hold the maximum acceleration of the bike. This is created from the self.__num_gears variable and is used to keep the self.__current_gear from exceeding the value.
    self.__current_gear - This variable is used to create the self.__acceleration variable along with self.__current_speed which are the current speed and acceleration of the bike. This can be updated with the change gear function.
    self.__acceleration - This variable is created in the constructor and is defaulted to 0. It is updated with the __update_acceleration, which is called on in the increase_speed function along with the set_num_of_gears function
        self.__current_speed - This variable is created in the constructor and is defaulted to 0. It can be updated with the increase speed function and is updated based on the self.__current_gear variable, self.__num_gears variable and self.__acceleration variables.
There is 1 class variable.
    __number_of_wheels - This holds the value of the number of wheels of the bicycle. This can be a class variable as all bikes have the same number of wheels.
There are a total of 7 getter functions for all the private variables:
    get_name - This function takes in self as an argument. All it is meant to do is to access the private variable self.__name. The function get_name returns self.__name for the user of the class to access the name of the bike.
    get_gears - This function takes in self as an argument. All it is meant to do is to access the private variable self.__num_gears. The function get_gears returns self.__num_gears for the user of the class to access the total number of gears of the bike.
    get_max_speed - This function takes in self as an argument. All it is meant to do is to access the private variable self.__max_speed. The function get_max_speed returns self.__max_speed for the user of the class to access the max speed of the bike.
    get_speed - This function takes in self as an argument. All it is meant to do is to access the private variable self.__current_speed. The function get_speed returns self.__current_speed for the user of the class to access the current speed of the bike.
    get_number_of_wheels - This function takes in self as an argument. All it is meant to do is to access the private variable self.__number_of_wheels. The function get_number_of_wheels returns self.__number_of_wheels for the user of the class to access the number of wheels of the bike.
    get_acceleration - This function takes in self as an argument. All it is meant to do is to access the private variable self.__acceleration. The function get_acceleration returns self.__acceleration for the user of the class to access the current acceleration of the bike.
    get_current_gear - This function takes in self as an argument. All it is meant to do is to access the private variable self.__current_gear. The function get_current_gear returns self.__current_gear for the user of the class to access the current gear of the bike.
There are a total of two setter functions, set_name and set_num_of_gears.
    set_name - This function allows the user of the class to change the private instance variable __name. This takes in the arguments self and the parameter name which is cast as a string. If name can't be cast into a string, then the function accepts value error, and does not chance self.__name. There are two possible returns. If the argument name can not be turned into a string, and the function accepts value error, the function returns None after printing an error message. If name can become a string, then the function returns the updated value of self.__name.
    set_num_of_gears - This function allows the user to change the total number of gears in the bicycle class. This takes in two arguments: self and the new number of gears (gears), which should be an int. The value Gears gets cast to an int, at the beginning of the function in a try except statement. If gears can't be cast as an int, then it accepts ValueError and returns None. If the value gears can be cast to an int, then self.__num_gears is set to gears. Becasue there are instance variables that rely on the value of self.__num_gears, there are three helper functions that change the state of self.__max_acceleration, self.__acceleration, and self.__max_speed to how they were set up in the constructor, along with setting the two other instance variables to their original value in the constructor. This will then return the updated value of self.__num_gears.
There are a total of 3 helper functions to update values after changing instance variables with setter function set_num_of_gears. These are all private methods, as they are only needed inside the class, when the value of either self.__num_gears or self.__current_gear are changed:
    __update_max_acceleration - This function is called in the set_num_of_gears function to update the value of self.__max_acceleration to how it was set up in the constructor, based on the new self.__num_gears value. This function only takes in self as an argument, and returns the updated value of self.__max_acceleration.
    __update_acceleration - This function is called in the set_num_of_gears function to update the value of self.__max_acceleration to how it was set up in the constructor, based on the new self.__num_gears value. This function is also called in another function that updates the current gear, which changes the acceleration. This function only takes in self as an argument, and returns the updated value of self.__acceleration.
    __update_max_speed - This function is called in the set_num_of_gears function to update the value of self.__max_speed to how it was set up in the constructor, based on the new self.__num_gears value. This function only takes in self as an argument, and returns the updated value of self.__max_speed.
There are two other functions that add other functionality to the class:
    change_gear - This function increases or decreases the gear value. This takes in an argument of a string and self. It either increases it or decreases it by 1. The string can only be "+" and "-". If not it puts an error message in the console, amd returns the original __current_gear.
    increase_speed - This function only takes in self as an argument. This function's purpose is to increase th current speed of the bike which is held in the variable self.__current_speed. This increases the value based on the value of self.__max_speed, self.__max_acceleration, and self.__acceleration.

    My demo program in the main function simulates a race and prints different information about the bikes with the
getter functions. It creates three bikes, and stores them in a list. In a separate list, it stores the positions of the
bikes, which the speed is added to every time each bike moves on one pass through the for loop. The for loop also calls
change_gear where a random input that is chosen between "+" and "-" with the random module. Also increase_speed is
called to make the gear change increase the speed value which is then added to the position. Each pass through the while
loop, the first place position is updated to the index of the bike with the furthest position. Once a winner is decided,
it prints out the name of the bike of the winner with get_name and then prints out the other information about all the
bikes, and then the program ends. All the user need to do to run the demo program is to run the main method in the class