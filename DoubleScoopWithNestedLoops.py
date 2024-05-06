# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the 
# week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the 
# times of the day. For each time, randomly select a mood from a predefined list and print it.

import random

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
time_of_day = ["morning", "afternoon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for i in range(len(days)):
    day = days[i]
    for i in range(len(time_of_day)):
        time = time_of_day[i]
        mood = random.choice(moods)
        print(f"On {day} during the {time} you were feeling {mood}.")

