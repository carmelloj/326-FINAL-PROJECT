#326-Main-File

"""Workout Planner Code! You input your days per week, your current exercise level, and any parts that you'd like to focus on!
    We will present you with a week worth of workouts pertaining to your needs and show you how to move forward. The code will
    use regular expressions to call the data from the workout_database text file and print the data to the user.
"""

#How I want the code to print:
"""Here is your workout plan for the next {number} days!

#Monday: 

#Focus: Glutes

# 2x10 reps of ___
# 3x15 reps of ___
# QUICK WATER BREAK (5 MINUTES)
# -FINISH EXERCISE

#Tuesday:

#BREAK

#Wednesday: 
# 
# Focus: Balance

# 2x10 reps of ___
# 3x15 reps of ___
# QUICK WATER BREAK (5 MINUTES)
# -FINISH EXERCISE

#Thursday:
#BREAK

etc..
"""
class Workouts:
    """This class contains all the workout information from each section of our workout code.
    
    Args:
    focus (str): the area you'd like to focus your workout on
    days (int): the amount of days per week you'd like to workout
    difficulty (str): the difficulty of the workout you'd like to do

    """
    def __init__(self, focus, days, difficulty):
        self.focus = focus
        self.days = days
        self.difficulty = difficulty

    def adding_workout(self):
        """Adding a workout to the weekly schedule. Gets the workout info from the Workout_Info Class

        Returns:
        The workout for that day
        
        Use self.days and self.focus in the code!
        """

        pass

    def workout_days(self): 
        """ Picks the amount of days throughout the week you want to workout and passes it to adding_workout function
        """
        pass

    def workout_difficulty(self):
        """Gets the workout difficulty from the user and passes it to adding_workout function
        """
        pass

    def print_workout_schedule(self): 
        """Returns the workout schedule generated from the Workout class using f strings"""
        workouts = []
        #BASED OFF THE REQUEST FROM
        if self.days >= 1:
            #workouts.append(Workout_Info.{focus}) is the structure we're going for
            print("ABC") #PULL IN THE INFO FROM THE WORKOUT SECTION THEY WANTED AND PRINT
        elif self.days >= 2:
            print("ABC") #
        elif self.days >= 3:
            print("ABC")
        elif self.days >= 4:
            print("ABC")
        elif self.days >= 5:
            print("ABC")

        return f'Here is your workout plan for the next week!' #UPDATE WITH THE REST OF THE CODE ONCE FUNCTIONS ARE BETTER UPDATED
        pass













    def main():
        print("Welcome to your personalized workout routine! Allow ud to help you by entering the following information.\n")
        difficulty = input("What would you say your workout level is at? (Beginner, Intermediate, Advacned)")
        days = input("How many dyas a week would you prefer to workout? Maximum of 5.")
        focus = input("Are there any areas youd like to focus on? \nWe have specificatins for Arms, Legs, Back, Glutes &Abs.\nIf you have no specifications type 'Balanced' ")

        workout = Workouts(focus, days, difficulty)
        workout.adding_workout()
        workout.workout_difficulty()
        workout.print_workout_schedule()

    if __name__ == "__main__":
     main()

    #UNIT TESTS

    #The unit tests makes sure that each of the focus area prints out correctly for each difficulty 

    #If the user were to want arms at an intermediate level then it must retunr the right information (regualr expressions)

    # The workout schedule must have certain days as breaks depending on how many days they want to workout

    #For example, if they want to workout for four days, there must be a break on Wednesday and Saturday














