import re
#326 FINAL PROJECT
 

#MUST HAVE 8 ORIGINAL FUNCTIONS, TWO PER TEAM MEMBER

"""Workout Planner Code! You input your days per week, your current exercise level, and any parts that you'd like to focus on!
    We will present you with a week worth of workouts pertaining to your needs and show you how to move forward. The code will
    use regular expressions to call the data from the workout_database text file and print the data to the user.

"""
#COMMITING CHANGES
class Workouts: #Carmello
    """This class contains all the workout information from each section of our workout code.
    
    Args:
    focus (str): the area you'd like to focus your workout on
    days (int): the amount of days per week you'd like to workout
    difficulty (str): the difficulty of the workout you'd like to do

    """
    def __init__(self, focus, days, difficulty): #Carmello
        self.focus = focus.lower()
        self.days = int(days)
        self.difficulty = difficulty.lower()
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.info = Workout_Info(difficulty)

    def adding_workout(self): #Carmello
        """Adding a workout to the weekly schedule. Gets the workout info from the Workout_Info Class

        Returns:
        The workout for that day
        
        """
        if self.focus == "arms":
            return self.info.arms()
        elif self.focus == "legs":
            return self.info.legs()
        elif self.focus == "glutes":
            return self.info.glutes()
        elif self.focus == "back":
            return self.info.back()
        elif self.focus == "abs":
            return self.info.abs()
        elif self.focus == "WARM_UP":
            return self.info.warm_up()
        else:
            return self.info.balanced()


    def workout_days(self): #Carmello
        """ Picks the amount of days throughout the week you want to workout and passes it to adding_workout function


        Returns the days throughout the week that you'll workout
        """
        if int(self.days) == 4: #We want specific days for 4 days.
            return ['Monday', 'Wednesday', 'Friday', 'Sunday']
        if self.days == 5 and self.difficulty == "advanced": 
            #if they are doing an advanced workout, the days need to be spaced more for recovery
            return ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Sunday']

        intervals = len(self.days_of_week) // self.days
        final_days = [self.days_of_week[i * intervals] for i in range(self.days)] #evenly spaces out the workout days throughout the week
        return final_days
    
    

    def workout_difficulty(self): #Carmello
        """Gets the workout difficulty from the user and passes it to adding_workout function

         Returns: the difficulty in lowercase

        """
        return self.difficulty.lower()

    def print_workout_schedule(self): #Carmello
        """Prints the workout schedule generated from the Workout class line by line. This is the main code that will be printed out to the user
       
        """
        work_days = self.workout_days()
        work_plan = self.adding_workout()
        warm_ups = self.info.warm_up()

        print(f'\nHere is your workout plan for the next {self.days} days: \n')

        for day in self.days_of_week[:7]:
            print(f"{day}:")
            if day in work_days:
                print(f"\nFocus: {self.focus.capitalize()}")
                print("WARM-UP:")
                for line in warm_ups:
                    print(line)
                print("\nMAIN WORKOUT:")
                for i, line in enumerate(work_plan):
                    print(f"{line}")
                    if i % 2 == 0:
                        print("QUICK WATER BREAK (2 MINUTES)")
                print("FINISHED\n")
            else:
                print("BREAK\n")


class Workout_Info(): #Zola
    """
    Has the information for every part of the workout that will be returned to the main Workout class and printed
   
    Args:
    difficulty (str): the difficulty of the workout (beginner, intermediate, advanced)

    
    """
    def __init__(self, difficulty): 
        self.difficulty = difficulty.lower()
        with open("Workout_Database.txt","r") as f:
            self.data = f.read()

    def arms(self):
        """Using regular expression to find the arms part of the database and returning the information to the workout script
       
        Returns: the workout data from the arms section
        """

        """Using regular expression to find the arms part of the database and returning the information to the workout script"""
        return self.get_workout_data("arms")

    def legs(self):
        """Using regular expression to find the legs part of the database and returning the information to the workout script"""
        return self.get_workout_data("legs")

    def glutes(self):
        """Using regular expression to find the glutes part of the database and returning the information to the workout script"""
        return self.get_workout_data("glutes")

    def back(self):
        """Using regular expression to find the back part of the database and returning the information to the workout script"""
        return self.get_workout_data("back")

    def abs(self):
        """Using regular expression to find the abs part of the database and returning the information to the workout script"""
        return self.get_workout_data("abs")

    def balanced(self):
        """Using regular expression to find the balanced part of the database and returning the information to the workout script"""
        return self.get_workout_data("balanced")
    
    def warm_up(self):
        """Using regular expression to find the balanced part of the database and returning the information to the workout script"""
        return self.get_workout_data("WARM-UP")
    
    def get_workout_data(self,focus_area):
        """Gets workout data based on the focus area that the user requested. Regular expressions are
           used to extract the exact data from the Workout_Database file.

        Args:
        focus_area (str): the area the user requested to focus on

        Returns:
        The data from the Workout_Database file cirresponding with the requested focus area.
        """

        #this code assumes that all data is correctly input based on the instructions given in the terminal
        #print(self.data) <-- makes sure whole data is printing
        pattern = rf"#\s*{focus_area.lower()}\s*{self.difficulty}\s*\n(.*?)(?=\n#|\Z)"
        if focus_area == "WARM-UP":
            pattern = rf"#WARM-UP\n(.*?)(?=\n#|\Z)"
        match = re.search(pattern, self.data, re.DOTALL|re.IGNORECASE)
        return match.group(1).strip().split('\n')



def main(): #Edom
    """Main function where the user is prompt with the questions that give us the data needed to print the workout"""

    print("Welcome to your personalized workout routine! Allow us to help you by entering the following infomration.\n")
    difficulty = input("What would you say your workout level is at? (Beginner, Intermediate, Advanced) ")
    days = input("How many days a week would you prefer to workout? Maximum of 5. ")
    focus = input("Are there any areas you'd like to focus on? \nWe have specifications for: Arms, Legs, Back, Glutes & Abs.\nIf you have no specifications, please type 'Balanced' ")

    workout = Workouts(focus, days, difficulty)
    workout.adding_workout()
    workout.workout_days()
    workout.workout_difficulty()
    workout.print_workout_schedule()


#Unit Tests 
def test_workouts():
 # 3 days, arms workout, and intermediate workout
    workout = Workouts("arms", 3, "Intermediate")
    days = workout.workout_days()
    expected_days = ['Monday', 'Wednesday', 'Friday']
    assert days == expected_days, f"Expected{expected_days}, but got {days}"


    #Testing 4 days, abs workout, and beginner
    workout_4 = Workouts("abs",4,"beginner")
    days_4 = workout_4.workout_days()
    expected_4 =  ['Monday', 'Wednesday', 'Friday', 'Sunday']
    assert days_4 == expected_4,f"4-day workout: expected{expected_4},got{days_4}"


    #Testing different wording to make sure caps doesn't affect the result
    workout_wording = Workouts("Legs", 3, "AdVanCed")
    difficulty = workout_wording.workout_difficulty()
    expected_diff = "advanced"
    assert difficulty == expected_diff, f"Expected difficulty '{expected_diff}', but got '{difficulty}'"

    #Testing balanced, 2 day, advanced
    workout_2 = Workouts("Balanced", 2, "ADVANCED")
    days_2 = workout_2.workout_days()
    expected_2 = ['Monday', 'Thursday']
    assert days_2 == expected_2, f"2-day workout: expected {expected_2}, but got {days_2}"


if __name__ == "__main__":
    main()
    test_workouts()